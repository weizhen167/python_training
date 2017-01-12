#!/usr/bin/env python

import os
import subprocess
import sys
from fontTools import ttLib


# What we want to do is take in a directory. For all the pdf files in that
# directory, and find out what fonts they have embedded. If they match one of
# our source font files, we want to replace the font in the pdf with our
# source font; this is done by recording that relation in the centralization
# font file, and passing the centralization font file with -q when normalizing
class CentralizeFonts:
    # Some font files may lead with /, _, etc, which aren't in the font name
    # Any character in this will be stripped from the start of the font name
    remove_leading = " \\/_"

    # Init method, also reads in all the source fonts for later use
    def __init__(self, source_font_dir, ttf_out_dir):
        # Where we record which pdf fonts match a source font; this is used
        # later to construct the font centralization file
        self.font_match = {}

        # The source font directory, where all of the source fonts used for
        # replacement reside. Probably is (opInstall)/common/fontttf
        self.source_font_dir = source_font_dir

        # CentralizeFonts writes out pdf fonts to this directory, using
        # pdf_parser.py, so it can compare the font names contained internally
        self.ttf_out_dir = ttf_out_dir

        # If you want, you can provide a file containing variations on font
        # names (times, times-roman, etc. for Times New Roman, for example).
        # During the matching by filename, it'll accept any of those variations
        self.accepted_variants = {}

        # A dictionary that will be filled later. Use a font filename as a key,
        # and it will return the name of the font that file contains
        self.font_to_name = {}

        # Any errors that occur while building the centralization file should
        # be recorded here; can print them all at end for easier reading
        self.errors_list = []

        # Filling in font_to_name here
        for font_file in os.listdir(self.source_font_dir):
            if font_file.endswith(".ttf"):
                try:
                    tt = ttLib.TTFont(os.path.join(self.source_font_dir,
                                                   font_file))
                    self.font_to_name[font_file] = self.read_ttf_name(tt)[0]
                except ttLib.TTLibError:
                    self.print_error("\tError while reading",
                                     font_file,
                                     "as a ttf file")
            elif font_file.endswith(".pfb"):
                try:
                    self.font_to_name[font_file] = \
                        self.read_pfb_name(os.path.join(self.source_font_dir,
                                                        font_file))[0]
                except IOError:
                    self.print_error("\tError while reading",
                                     font_file,
                                     "as a pfb file")
            else:
                print "\tFile is not a ttf or pfb file"

    # Just a quick method to add any error messages we write to the errors list
    # after printing them
    def print_error(self, *args):
        error_message = " ".join(args)
        print error_message
        self.errors_list.append(error_message)

    # Given a pfb file, we want to read:
    # - The font name itself, so we can match it with the pdf fonts
    # - The font family, so we can keep that structure intact when creating
    #   the centralization font file
    # - The font style, for similar reasons
    def read_pfb_name(self, font):
        font_name = ""
        font_family = ""
        weight = ""
        angle = "0"
        font_style = ""

        with open(font, "r") as font_fd:
            contents = font_fd.read()
            if "/FontName" in contents:
                font_name_start = contents.find("/FontName")
                font_name_end = contents.find("def", font_name_start)
                font_name = contents[font_name_start:font_name_end]\
                    .split(" ", 1)[1]\
                    .lstrip("/")\
                    .rstrip(" ")

            if "/FamilyName" in contents:
                font_family_start = contents.find("/FamilyName")
                font_family_start += contents[font_family_start:].find("(")
                font_family_end = contents.find(")", font_family_start)
                font_family = contents[font_family_start:font_family_end]\
                    .lstrip("(") \
                    .rstrip(")")

            if "/Weight" in contents:
                weight_start = contents.find("/Weight")
                weight_start += contents[font_family_start:].find("(")
                weight_end = contents.find(")", weight_start)
                weight = contents[font_family_start:font_family_end] \
                    .lstrip("(") \
                    .rstrip(")")

            if "/ItalicAngle" in contents:
                angle_start = contents.find("/ItalicAngle")
                angle_start += contents[angle_start:].find(" ")
                angle_end = contents.find(" ", angle_start+1)
                angle = contents[angle_start:angle_end].strip(" ")

            if "bold" in weight.lower():
                font_style += "Bold "

            if int(angle) != 0:
                font_style += "Italic "

        return font_name, font_family, font_style

    # Given a ttf file instead, we want to gather the same information
    def read_ttf_name(self, font):
        """Get the short name from the font's names table"""
        FONT_SPECIFIER_NAME_ID = 4
        FONT_SPECIFIER_STYLE_ID = 2
        FONT_SPECIFIER_FAMILY_ID = 1
        name = ""
        family = ""
        style = ""

        for record in font['name'].names:
            if record.nameID == FONT_SPECIFIER_NAME_ID and not name:
                if '\000' in record.string:
                    name = unicode(record.string, 'utf-16-be').encode('utf-8')
                else:
                    name = record.string
            elif record.nameID == FONT_SPECIFIER_FAMILY_ID and not family:
                if '\000' in record.string:
                    family = unicode(record.string, 'utf-16-be').encode('utf-8')
                else:
                    family = record.string
            elif record.nameID == FONT_SPECIFIER_STYLE_ID and not style:
                if '\000' in record.string:
                    style = unicode(record.string, 'utf-16-be').encode('utf-8')
                else:
                    style = record.string
            if name and family and style:
                break
        return name, family, style

    # Given the name of a pdf font and it's matching source font filename, adds
    # the relationship to font_match
    def record_match(self, pdf_font_name, source_font_filename, font_filename = ""):
        # The structure of font_match is as follows:
        #   - Dictionary (key is the font family the source font belongs to)
        #    - Dictionary (key is a source font within the font family)
        #     - tuple containing:
        #       - The font file for the source font
        #       - set of all substitute pdf font names
        #       - The font style
        #print pdf_font_name
        source_font_filepath = os.path.join(self.source_font_dir,
                                            source_font_filename)

        if source_font_filename.endswith(".ttf"):
            try:
                font_file = ttLib.TTFont(source_font_filepath)
            except ttLib.TTLibError:
                self.print_error("\tError while reading",
                                 source_font_filename,
                                 "as a ttf file")
                return

            source_font, source_family, source_style = self.read_ttf_name(font_file)
        elif source_font_filename.endswith(".pfb"):
            try:
                source_font, source_family, source_style = \
                    self.read_pfb_name(os.path.join(self.source_font_dir,
                                                    source_font_filename))
            except IOError:
                self.print_error("\tError while reading",
                                 source_font_filename,
                                 "as a pfb file")

        if source_family not in self.font_match.keys():
            self.font_match[source_family] = {}

        family = self.font_match[source_family]
        if source_font not in family.keys():
            family[source_font] = (source_font_filename, set(), source_style)
            family[source_font][1].add(source_font)

        if "," in pdf_font_name:
            self.print_error("\tWarning:",
                             pdf_font_name,
                             "has a comma in it.",
                             "You will need to edit the centralization file"
                             " afterwards.")
        family[source_font][1].add(pdf_font_name)

        if font_filename:
            font_f_stripped = font_filename.rsplit(".", 1)[0]
            font_f_stripped = font_f_stripped.lstrip(self.remove_leading)

            if "," in font_f_stripped:
                self.print_error("\tWarning:",
                                 font_f_stripped,
                                 "has a comma in it.",
                                 "You will need to edit the centralization "
                                 "file afterwards.")
            family[source_font][1].add(font_f_stripped)

    # Some font files, like for Times New Roman, might themselves have variants
    # in their naming (such as times.ttf); this will read in a variants file and
    # allow checking for variants on the font file name, if any exist
    def read_accepted_variants(self, variants_file):
        # The format of a variants file is as follows:
        # [font_name]:[font_name_variant1_],[font_name_variant_2],...

        with open(variants_file, "r") as var_fd:
            for line in var_fd:
                font_name, substitutions = line.strip("\n").split(":", 1)
                font_name = font_name.strip(" ")

                if font_name not in self.accepted_variants.keys():
                    self.accepted_variants[font_name] = set()

                for sub_name in substitutions.split(","):
                    sub_name = sub_name.strip(" ")
                    self.accepted_variants[font_name].add(sub_name.lower())

    # Attempts to find font match just with the filenames; if no match is found,
    # write out the font file to ttf_out_dir
    def initial_matching(self, pdf_dir):
        print "\nMatching pdf fonts to source font files by external name\n"

        for pdf_file in os.listdir(pdf_dir):
            pdf_filepath = os.path.join(pdf_dir, pdf_file)
            print pdf_file
            font1 = subprocess.Popen("python pdf-parser.py -s FontFile \"{0}\""
                                     .format(pdf_filepath),
                                     stdout=subprocess.PIPE).communicate()[0]

            font_id_set = set()

            for line in font1.split(">>"):
                if "Referencing" in line and "FontName" in line:
                    ref_index = line.find("Referencing")
                    space_before_index = line.find(" ", ref_index)
                    space_after_index = line.find(" ", space_before_index + 1)
                    font_id = line[space_before_index+1:space_after_index]

                    name_index = line.find("FontName")
                    sb_index = line.find(" ", name_index)
                    sa_index = line.find("\n", sb_index + 1)
                    font_name = line[sb_index+2:sa_index]

                    font_id_set.add((font_id, font_name))

            for font_id, font_name in font_id_set:
                # Sometimes, it will have a carriage return in the name
                font_name = font_name.strip("\r\n")
                print "\t", font_name

                font_name_stripped = self.strip_font_name(font_name)

                found_match = False
                for file_name in os.listdir(self.source_font_dir):
                    file_name_stripped = file_name.rsplit(".", 1)[0]

                    file_font_name = self.font_to_name.get(file_name, "")
                    if file_name_stripped.lower() == font_name_stripped.lower() or \
                       font_name_stripped.lower() in self.accepted_variants.get(file_font_name, []):
                        found_match = True
                        print "\t\tFound match:", file_name
                        self.record_match(font_name, file_name, file_name)
                        #self.font_match[font_name_stripped] = file_name
                        break

                # If no match was found, extract the font from the pdf
                if not found_match:
                    font2 = subprocess.Popen("python pdf-parser.py -o {1} -f -d \"{2}\" \"{0}\""
                                             .format(pdf_filepath, font_id,
                                                     os.path.join(self.ttf_out_dir,
                                                                  font_name + ".ttf")),
                                             stdout=subprocess.PIPE).communicate()[0]

    # For those whose filenames didn't match directly, see if their font file
    # contains a name that matches one of the source font files
    def find_matching_tff(self):
        print "\nMatching pdf fonts to source font files by internal name\n"

        for font_file in os.listdir(self.ttf_out_dir):
            print font_file
            try:
                tt = ttLib.TTFont(
                    os.path.join(self.ttf_out_dir, font_file))

                font_name = self.read_ttf_name(tt)[0]

                # Covers cases where the naming scheme carries over to
                # the font file
                font_name_stripped = self.strip_font_name(font_name)

                for ttf_name in self.font_to_name:
                    if font_name.lower() == self.font_to_name[ttf_name].lower() \
                            or font_name_stripped.lower() == self.font_to_name[ttf_name].lower():
                        print "\tFound match:", font_file, "to", ttf_name
                        self.record_match(font_name, ttf_name, font_file)
            except ttLib.TTLibError:
                self.print_error("\tError while reading", font_file)

    # Uses the current font matches to put together a substitution file (like
    # hp.fnt) to use for centralization
    def build_substitution_file(self, sub_path):
        print "\nBuilding file...\n"

        with open(sub_path, "w") as sub_fd:
            for font_family in self.font_match:
                print font_family
                for index, font_name in enumerate(sorted(self.font_match[font_family].keys())):
                    print "\t", font_name
                    ttf_name, substitutes, style = self.font_match[font_family][font_name]

                    sub_fd.write("[{0}]\n".format(font_name))

                    # family
                    print "\t\t", font_family
                    sub_fd.write("\tfamily={0}\n".format(font_family))

                    # substitute
                    sub_fd.write("\tsubstitute=" + ",".join(substitutes) + "\n")

                    for pdf_font in substitutes:
                        print "\t\t", pdf_font

                    # style
                    if "bold" in style.lower() and "italic" in style.lower():
                        sub_fd.write("\tstyle=gras,italique\n")
                    elif "bold" in style.lower():
                        sub_fd.write("\tstyle=gras\n")
                    elif "italique" in style.lower():
                        sub_fd.write("\tstyle=italique\n")
                    else:
                        sub_fd.write("\tstyle=normal\n")

                    # size
                    sub_fd.write("\tsize=*\n")

                    # file
                    sub_fd.write("\tfile={0}\n".format(ttf_name))

                    #dynamic
                    sub_fd.write("\tdynamic=1\n\n")

    # Prints all the errors that occurred at the end, so a human can check and
    # use them to check for problems with the substitution font file produced
    def print_errors(self):
        if len(self.errors_list) == 0:
            print "\nNo errors found!"
            return

        print "\nPrinting all errors:"
        for error in self.errors_list:
            print error

    # Method to strip the font name down to it's base component
    # ex: UTRMYK+TimesNewRomanPSMT -> TimesNewRomanPSMT
    def strip_font_name(self, font_name):
        font_name_stripped = font_name

        if "+" in font_name:
            font_name_stripped = font_name_stripped.split("+", 1)[1]
        return font_name_stripped

if __name__ == '__main__':
    args = sys.argv[1:]
    if "-h" in args:
        print "Usage: ./centralize_fonts [-options]"
        print "-f: source font folder (The source fonts to substitute in)"
        print "-p: pdf font folder (Where pdf fonts should be written to)"
        print "-v: variant file path (path containing variants on file names)"
        print "-i: pdf input directory (folder containing pdfs to centralize)"
        print "-o: centralization font file path (where to write fnt file to)"
        exit(0)

    args_iter = iter(args)
    args_dict = dict(zip(args_iter, args_iter))

    run_directory = os.path.dirname(os.path.abspath(__file__))

    # Get options or revert to defaults
    source_font_dir = args_dict.get("-f", os.path.join(run_directory,
                                                       "fontttf"))
    pdf_font_dir = args_dict.get("-p", os.path.join(run_directory,
                                                    "pdfttf"))
    variants_file = args_dict.get("-v", os.path.join(run_directory,
                                                     "substitutions.txt"))
    pdf_filepath = args_dict.get("-i", os.path.join(run_directory,
                                                    "pdfs"))
    output_dir = args_dict.get("-o", os.path.join(run_directory,
                                                  "font_centralization.fnt"))

    centralize_fonts = CentralizeFonts(source_font_dir,
                                       pdf_font_dir)
    centralize_fonts.read_accepted_variants(variants_file)
    centralize_fonts.initial_matching(pdf_filepath)
    centralize_fonts.find_matching_tff()
    centralize_fonts.build_substitution_file(output_dir)
    centralize_fonts.print_errors()
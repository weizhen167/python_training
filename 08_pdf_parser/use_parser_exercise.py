import subprocess

# Output from the help command
'''
Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -s SEARCH, --search=SEARCH
                        string to search in indirect objects (except streams)
  -f, --filter          pass stream object through filters (FlateDecode,
                        ASCIIHexDecode, ASCII85Decode, LZWDecode and
                        RunLengthDecode only)
  -o OBJECT, --object=OBJECT
                        id of indirect object to select (version independent)
  -r REFERENCE, --reference=REFERENCE
                        id of indirect object being referenced (version
                        independent)
  -e ELEMENTS, --elements=ELEMENTS
                        type of elements to select (cxtsi)
  -w, --raw             raw output for data and filters
  -a, --stats           display stats for pdf document
  -t TYPE, --type=TYPE  type of indirect object to select
  -v, --verbose         display malformed PDF elements
  -x EXTRACT, --extract=EXTRACT
                        filename to extract malformed content to
  -H, --hash            display hash of objects
  -n, --nocanonicalizedoutput
                        do not canonicalize the output
  -d DUMP, --dump=DUMP  filename to dump stream content to
  -D, --debug           display debug info
  -c, --content         display the content for objects without streams or
                        with streams without filters
  --searchstream=SEARCHSTREAM
                        string to search in streams
  --unfiltered          search in unfiltered streams
  --casesensitive       case sensitive search in streams
  --regex               use regex to search in streams
  -g, --generate        generate a Python program that creates the parsed PDF
                        file
  --generateembedded=GENERATEEMBEDDED
                        generate a Python program that embeds the selected
                        indirect object as a file
  -y YARA, --yara=YARA  YARA rule (or directory or @file) to check streams
                        (can be used with option --unfiltered)
  --yarastrings         Print YARA strings
  --decoders=DECODERS   decoders to load (separate decoders with a comma , ;
                        @file supported)
  --decoderoptions=DECODEROPTIONS
                        options for the decoder
'''

# Example 1: Simply read the file


# Example 2: Search for an object with the given phrase
output = subprocess.check_output('pdf-parser.py hello-world.pdf', shell=True)

output = subprocess.check_output('pdf-parser.py hello-world.pdf -s Font', shell=True)


# Example 3: Get a specific object

output = subprocess.check_output('pdf-parser.py hello-world.pdf -o 7', shell=True)
# Example 4: Get references to that object
output = subprocess.check_output('pdf-parser.py hello-world.pdf -r 7', shell=True)

# Example 5: Get output from the stream

output = subprocess.check_output('pdf-parser.py hello-world.pdf -o 5 -d out.txt', shell=True)
# Example 6: Search within streams
output = subprocess.check_output('pdf-parser.py hello-world.pdf --searchstream "hello world"', shell=True)

# Example 7: Get a picture from the file
output = subprocess.check_output('pdf-parser.py Fonts_example.pdf -s Image', shell=True)

output = subprocess.check_output('pdf-parser.py Fonts_example.pdf -o 13 -d out.jpg', shell=True)
print output
import xml.etree.ElementTree as ET

import warnings
warnings.filterwarnings("ignore")


# Quick functions to print out a ET. Feel free to use it; it's here to show
# results later on in a readable manner
def rec_print(root):
    attr_text = ""
    for key in root.attrib:
        attr_text += " " + key + "=\"" + root.attrib[key] + "\""

    print "<{0}{1}>{2}".format(root.tag, attr_text, root.text or "").rstrip("\n\t ")
    for child in list(root):
        rec_print_h(child, 1)
    print "</{0}>".format(root.tag)


def rec_print_h(elem, tree_level):
    attr_text = ""
    for key in elem.attrib:
        attr_text += " " + key + "=\"" + elem.attrib[key] + "\""

    if not len(list(elem)):
        print "\t" * tree_level, "<{0}{1}>{2}</{0}>".format(elem.tag, attr_text, elem.text or "").rstrip("\n\t ")
    else:
        print "\t" * tree_level, "<{0}>{2}".format(elem.tag, attr_text, elem.text or "").rstrip("\n\t ")
        for child in list(elem):
            rec_print_h(child, tree_level + 1)
        print "\t" * tree_level, "</{0}>".format(elem.tag)


##### Methods of reading in the XML input ######

# A simple example of what an XML string might look like.
xml_string = """<Base>
    <JobId>123456</JobId>
    <JobPath>/adf/workdir/123456</JobPath>
    <Params>
        <Param name="abc">value1</Param>
        <Param name="xyz">value2</Param>
        <Param name="fhg">value3</Param>
    </Params>
</Base>
"""

# Parsing from a string
a = ET.fromstring(xml_string)
#rec_print(a)

# Parsing from a file
etree = ET.parse('weather.xml')
#rec_print(a.getroot())

##### Basic operations (create, read, update, delete) #####

# Get the root of a tree
root = etree.getroot()

# Iterate through the children



#for child in root: print child.tag



# Searching through a tree
print root.iter("dewpoint_f")
print root.find("dewpoint_f")
print root.findall("dewpoint_f")

# Element resolves to True or False, for if conditions

if root.find("dewpoint_f") is not None:
    print "yes"
else:
    print "no"








# Building that tree from the xml string
'''
xml_string = """<Base>
    <JobId>123456</JobId>
    <JobPath>/adf/workdir/123456</JobPath>
    <Params>
        <Param name="abc">value1</Param>
        <Param name="xyz">value2</Param>
        <Param name="fhg">value3</Param>
    </Params>
</Base>
"""
'''


xml_tree = ET.ElementTree(ET.Element('Base'))
sample_root = xml_tree.getroot()
job_elem = ET.SubElement(sample_root, "JobId")
job_elem.text = "123456"
job_path_elem = ET.SubElement(sample_root,"Job_path")
job_path_elem.text = '/adf/workdir/123456'

params = ET.SubElement(sample_root,"Params")

pars = {
    "abc":"value1",
    "xyz":"value2",
    "fhg":"value3"
}

for key in pars:
    param = ET.SubElement(params,"Param",{"name":key})
    param.text = pars[key]

rec_print(sample_root)

job_elem.text = "notice how this changed"
job_elem.set("example",'text')
job_elem.attrib['example2'] = 'text2'
job_elem.append(job_path_elem)
# rec_print(sample_root)

# Updating an element

# Removing an element
job_elem.remove(job_path_elem)
rec_print(sample_root)

# Write back to a string / file
# print ET.tostring(sample_root)
xml_tree.write('sample.xml')
#rec_print(xml_tree)


# To wrap things up, let's go into a little more detail with finding information
# in the tree. ElementTree has limited support for XPath, and can support the
# following expressions:

# tag
# *                 : all elements
# .                 : the current element
# //                : all subelements
# ..                : the parent element
# [@attrib]         : all elements with attribute 'attrib'
# [@attrib='value'] : all elements with attribute 'attrib' == 'value'
# [tag]             : all immediate children with the given tag name
# [tag='text']      : all immediate children with given tag name and text content
# [position]        : child element with given index

# Example 1: grandchildren with the given tag name
print sample_root.findall("./*/Param")
# Example 2: any element with name = abc
print sample_root.findall(".//*[@name='abc']")
# Example 3: The parent(s) of elements with tag 'Param'
print sample_root.findall(".//Param/..")
# Example 4: The last Param element
print sample_root.findall(".//Params/Param[last()]")[0].text

# Now, give it a try. There is a file called all_the_weather.xml, containing the
# same info as weather.xml, except for all measured locations in MA.
# Please do the following:
# - Get the average temperature (Fahrenheit)
# - Remove any instances of "garbage_tag"

# Return a float
def get_temp(xml_path):
    pass

# Return an etree
def remove_garbage_tag(xml_path):
    pass

# print get_temp('all_the_weather.xml')
# remove_garbage_tag('all_the_weather.xml').write('all_weather_cleaned.xml')
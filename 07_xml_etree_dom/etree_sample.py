import xml.etree.ElementTree as ET
import xml.dom.minidom as MD

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


#####  First, methods of reading in the XML input ######

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

# You can pass this to the fromstring method to get an ElementTree
tree = ET.fromstring(xml_string)

# weather.xml is from the National Oceanic and Atmospheric Administration; it's
# the measurements on 12/13/2016 in Logan International Airport, Boston, MA.
weather_tree = ET.parse('weather.xml')
# rec_print(weather_tree.getroot())


##### Then, let's move to basic operations (create, read, update, delete) #####

# First, reading. Let's show how to iterate through the tree structure
# and read data from a node / leaf
root = weather_tree.getroot()

# We could just iterate through the children...
for child in root:
    # print child.tag
    pass

# But if we're looking for something more specific, we usually want to use
# iter, find, or findall

# Iter will recurse through the element, and all it's subelements, to find all
# instances of a tag and store them in an iterator
for el in root.iter("windchill_f"): # This one is two levels down
    print el
# Find will return the first instance of a tag that it finds, one level down
# If not found, it will return None
print root.find("windchill_f") # This will be None

# Moving on, findall() will return all instances of a tag one level down
print root.findall("windchill_f")

# Worth noting: if using it for a condition, be careful; an element that has no
# subelements returns False
if root.find("windchill_f") is None: # good
    print "did not find 'windchill_f' one level down"

if root.find("temp_f"): # bad
    print "found 'temp_f'"
else:
    print "remember: no children means it returns as False"

# After that, let's show how to create by building the tree from xml_string
pars = {
    "abc":"value1",
    "xyz":"value2",
    "fhg":"value3"
}
xml_tree = ET.ElementTree(ET.Element("Base"))
sample_root = xml_tree.getroot()
job_elem = ET.SubElement(sample_root, "JobId")
job_elem.text = "123456"
job_path_elem = ET.SubElement(sample_root, "JobPath")
job_path_elem.text = "/adf/workdir/123456"
params = ET.SubElement(sample_root, "Params")

for key in pars:
    param = ET.SubElement(params, "Param", {"name": key})
    param.text = pars[key]

rec_print(sample_root)

# Update is largely the same, but let's show it, for sake of completeness
job_elem.text = "Notice how this has changed"
job_elem.set("example", "text")
job_elem.attrib["example2"] = "text2"
job_elem.append(job_path_elem)
# rec_print(sample_root)

# We can also delete a few nodes from that structure afterwards
job_elem.remove(job_path_elem)
# rec_print(sample_root)

# Now we need to know how to write back to a string or file
# print ET.tostring(sample_root)
# xml_tree.write('sample.xml')

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
sample_root.findall("./*/Param")

# Example 2: any element with name = abc
sample_root.findall(".//*[@name='abc']")

# Example 3: The parent(s) of elements with tag 'Param'
sample_root.findall(".//Param/..")

# Example 4: The last Param element
sample_root.findall("./Params/Param[last()]")

# Now, give it a try. There is a file called all_the_weather.xml, containing the
# same info as weather.xml, except for all measured locations in MA.
# Please do the following:
# - Get the average temperature (Fahrenheit)
# - Remove any instances of "garbage_tag"

def get_temp(xml_path):
    """Gets the average temperature"""
    e_tree = ET.parse(xml_path)
    root = e_tree.getroot()

    total_temp = 0
    num_temps = 0
    for temp in root.iter('temp_f'):
        total_temp += float(temp.text)
        num_temps += 1

    if num_temps:
        return total_temp / num_temps
    return "None found"


def remove_garbage_tag(xml_path):
    """Removes any instances of 'garbage tag'"""
    e_tree = ET.parse(xml_path)
    root = e_tree.getroot()

    #for current_observation in root.findall('current_observation'):
    #    for garbage_tag in current_observation.findall('garbage_tag'):
    #        print garbage_tag
    #        current_observation.remove(garbage_tag)

    for tag_with_garbage_child in root.findall(".//garbage_tag/.."):
        for garbage_child in tag_with_garbage_child.findall("garbage_tag"):
            tag_with_garbage_child.remove(garbage_child)

    return e_tree

# print get_temp('all_the_weather.xml')
# remove_garbage_tag('all_the_weather.xml').write('all_weather_cleaned.xml')

namespaces = {
    "xsd": "http://www.w3.org/2001/XMLSchema",
    "xsi": "http://www.w3.org/2001/XMLSchema-instance",
    "nons": "http://www.weather.gov/view/current_observation.xsd"
}

print root.find("windchill_f", namespaces)
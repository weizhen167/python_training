import xml.etree.ElementTree as et
import datetime
start = datetime.datetime.now()
tree = et.parse(r'exponential_entity.xml')
root = tree.getroot()
end = datetime.datetime.now()
print end - start

"""The idea behind this attack is to have several layers of Entity expansion, exponentially blowing up a file in size.
This would take up several GB and entirely too much processing time. This specific XML file starts as 475 bytes, but expands to 3GB when expanded."""

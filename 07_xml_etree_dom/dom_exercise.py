import xml.dom.minidom as md
from xml.dom.minidom import parse, parseString

# Get an empty document
dom = md.getDOMImplementation()
doc = dom.createDocument(None, "root",None)
root  = doc.childNodes[0]

# Add a child
root.appendChild(doc.createTextNode('Example text Node'))
root.appendChild(doc.createComment('Example comment'))
# Add a child before a given child
example = doc.createElement("example")
root.appendChild(example)
root.insertBefore(doc.createElement("example before example"),example)

# Add an attribute
root.setAttribute('ex','attr')



# Get an attribute
assert root.hasAttribute("ex")
assert root.getAttribute("ex") == 'attr'


# Find a node with a given tag
print root.getElementsByTagName("example")

# Parse using minidom
xml = '<myxml>Some data<empty/> some more data</myxml>'


dom2 = parseString(xml)
print dom2.toprettyxml()
print doc.toprettyxml()



dom3 = parse('weather.xml')
print dom3.toxml()
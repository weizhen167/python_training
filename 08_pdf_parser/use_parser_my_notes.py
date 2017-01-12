import subprocess

#Start with breakdown of hello-world.pdf, and how the pdf format works
# Important things to touch upon

'''
pdf-parser isn't so much a library as it is a script. It's on this list of
training materials mostly because it's a nice tool for parsing through pdf files
for specific information

Of note is how the pdf format works.
- Basically, you can think of it as a tree of objects.
- Open up hello-world.pdf
- Show the tree structure
    - Catalog references Outlines and Pages
    - Pages has each Page as a kid
    - Page references objects like Contents, ProcSet, Font, etc.
    - Font is standalone, often referenced by multiple objects
    - Streams contain any actual data, rather than metadata
'''

# Move on to the uses of pdf-parser. Some quick notes about the help output:
'''
Notes on help output options:
 -h: Shows this help message
 -f: Pass a stream object through filters
    (so if a stream is deflated, for example, it'll inflate it)
 -o: get an object with a specific id
 -r: gets the objects referencing the object with the specific id
 -w: shows the raw output as well
 -s: search within objects (not streams) for given text
'''

# Run some commands, to get a feel for how it works

# Example 1: Simply read the file
output = subprocess.check_output("pdf-parser.py hello-world.pdf", shell=True)

#output = subprocess.Popen("pdf-parser.py hello-world.pdf",
#                          stdout=subprocess.PIPE).communicate()[0]

# Example 2: Search for an object with the given phrase
output = subprocess.check_output("pdf-parser.py hello-world.pdf -s Font", shell=True)
# Example 3: Get a specific object
output = subprocess.check_output("pdf-parser.py hello-world.pdf -o 5", shell=True)

# Example 4: Get references to that object
output = subprocess.check_output("pdf-parser.py hello-world.pdf -o 5", shell=True)

# Example 5: Get output from the stream
output = subprocess.check_output("pdf-parser.py hello-world.pdf -o 5 -d out.txt", shell=True)

# Example 6: Search within streams
output = subprocess.check_output("pdf-parser.py hello-world.pdf --searchstream \"hello world""", shell=True)

# Example 7: Get a picture from the file
output = subprocess.check_output("pdf-parser.py Fonts_Example.pdf -s Image", shell=True)
print output

subprocess.check_output("pdf-parser.py Fonts_Example.pdf -o 13 -d out.jpg", shell=True)
import fnmatch
import glob
import os

import re

# Excersise 1 Capture all the csv files using glob 
csv_list = glob.glob("files/*.csv")
print csv_list

# Excersise 2 Capture all of the "e" text files  glob iterator 
ite = glob.iglob("files/textfile_?e.txt")
for file in ite:
    pass
    print file

# Excersise 3 Capture all csv files 2-5 using fnmatch 
files = os.listdir('files/')
print [file for file in files if fnmatch.fnmatch(file,'csvfile_[2-5]*')]

# Excersise 4 Capture all the Text files 1-2 c and e fnmatch filter 
print fnmatch.filter(files,'textfile_[1-2][c-e]*')

# Excersise 5 Regex conversion.
regex =  fnmatch.translate('textfile_[1-2][ce]*')
re_obj = re.compile(regex)
print [file for file in files if re_obj.match(file)]






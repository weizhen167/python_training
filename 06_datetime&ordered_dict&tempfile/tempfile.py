import os
import tempfile

tmp = tempfile.TemporaryFile(mode='w+b')
try:
    tmp.write('Python Modules\nTempFile')
    tmp.seek(0)

    print tmp.read()
finally:
    tmp.close()

# Standard file manipulation
print '\nCustom FileName:'
filename = 'can_you_see_me.%s.txt' % os.getpid()  # Gets us a semi-random set of numbers
c_file = open(filename, 'w+b')
try:
    print 'c_file:', c_file
    print 'c_file name:', c_file.name
finally:
    c_file.close()
    # Delete file yourself
    os.remove(filename)

# Does not delete file when done
print
print 'mkstemp:'
temp = tempfile.mkstemp()
print temp
try:
    print 'temp:', temp
    print 'temp.name:', temp[1]
finally:
    pass

# It creates a file, and on platforms where it is possible, unlinks it immediately.
print
print 'TemporaryFile:'
temp2 = tempfile.TemporaryFile()
print temp2
try:
    print 'temp:', temp2
    print 'temp.name:', temp2.name
finally:
    pass

# The NamedTemporaryFile() function creates a file with a name, accessed from the name attribute.

print
print 'NamedTemporaryFile:'
temp3 = tempfile.NamedTemporaryFile()
print temp3
try:
    print 'temp:', temp3
    print 'temp.name:', temp3.name
finally:
    pass

	
	
	
	
	
	
# Linux output
# TempFile
# 
# Custom FileName:
# c_file: <open file 'can_you_see_me.3790.txt', mode 'w+b' at 0x7fb05093aae0>
# c_file name: can_you_see_me.3790.txt
# 
# mkstemp:
# (3, '/tmp/tmpD1pZmQ')
# temp: (3, '/tmp/tmpD1pZmQ')
# temp.name: /tmp/tmpD1pZmQ
# 
# TemporaryFile:
# <open file '<fdopen>', mode 'w+b' at 0x7fb05093ad20>
# temp: <open file '<fdopen>', mode 'w+b' at 0x7fb05093ad20>
# temp.name: <fdopen>
# 
# NamedTemporaryFile:
# <open file '<fdopen>', mode 'w+b' at 0x7fb05093ac90>
# temp: <open file '<fdopen>', mode 'w+b' at 0x7fb05093ac90>
# temp.name: /tmp/tmp7jxb_t
# jshatos@bender:~$
import traceback
import sys

# Using Traceback (traceback.print_exc, format_exc)
def create_exception(rec_level):
    if rec_level>0:
        create_exception(rec_level-1)
    else:
        print 1/0
try:
    create_exception(2)
except:
    print "no error found"
    #different format
    #error_string0 = traceback.print_exc(limit = 1)
    error_string1 = traceback.format_exc(limit=2)
    print error_string1
    #error_string2 = traceback.print_stack()


# Stack traces


def my_function(start):
    for i in range(start,100):
        return i

def my_generator(start):
    for i in range(start,100):
        yield i

print my_function(50)
print my_generator(50)

#for i in my_generator(50):
 #   print i

my_gen2 = my_generator(50)
print my_gen2
print my_gen2.next()
print my_gen2.next()


for i in my_gen2:
    print i
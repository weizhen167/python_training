import contextlib


# Create context without use of contextlib
class context_class(object):
    def  __init__(self):
        print 'init'
    def __enter__(self):
        print 'enter'
        return self
    def __exit__(self,exc_type, exc_val,exc_tb):
        print 'exit'

with context_class() as a:
    print 'in the context'
# Create context with context lib
@contextlib.contextmanager
def xml_tag(tag_name):
    print '<%s>' %tag_name
    yield tag_name
    print '</%s>' %tag_name

with xml_tag('tag_1'):
    print 'in the context'

# Nested contexts
@contextlib.contextmanager
def xml_tag_1(tag_name,fd):
    fd.write('<%s>\n' %tag_name)
    yield tag_name
    fd.write('\n</%s>' % tag_name)

with open("output.txt", "w") as fd:
    with xml_tag_1('tag_1',fd) :
        fd.write('hello_world')


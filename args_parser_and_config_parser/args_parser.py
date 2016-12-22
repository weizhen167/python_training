import argparse


#"C:\Users\zwei\Anaconda2\python.exe" C:\Users\zwei\Desktop\code\python_training\args_parser_and_config_parser\args_parser.py

# 01 intro
# what do we usually do?
'''
print "CMD is %s"  % (sys.argv)
print "length of args", len(sys.argv)
print "print each args"
for i, eachArg in enumerate(sys.argv):
    print "[%d] = %s" % (i, eachArg)
'''


# 02 basic use
#add help  parser.add_argument(dest = "echo", help = "echo the string you use here")
parser = argparse.ArgumentParser()


#parser.add_argument("test")
#parser.add_argument(dest = "test", help = "echo the string you use here")
#parser.add_argument(dest = "test", help = "echo the string you use here", type = int)
#parser.add_argument("-e", "--echo",dest = "test", help = "echo the string you use here", type = int)
#parser.add_argument("-e", "--echo",dest = "test", help = "echo the string you use here", choices=[0, 1, 2],type = int)
#parser.add_argument("-e", "--echo",dest = "test", help = "echo the string you use here", choices=[0, 1, 2],type = int,required=True)
#parser.add_argument("-e", "--echo",dest = "test", help = "echo the string you use here", default=False)


#03 actions
'''
parser.add_argument('-s', action='store', dest='simple_value',help='Store a simple value')
parser.add_argument('-c', action='store_const', dest='constant_value',const='value-to-store',
                    help='Store a constant value')
parser.add_argument('-t', action='store_true', default=False,dest='boolean_switch',
                    help='Set a switch to true')
parser.add_argument('-f', action='store_false', default=False,dest='boolean_switch',
                    help='Set a switch to false')
parser.add_argument('-a', action='append', dest='collection',default=[],help='Add repeated values to a list')
parser.add_argument('-A', action='append_const', dest='const_collection',const='value-1-to-append',default=[],
                    help='Add different values to list')
parser.add_argument('-B', action='append_const', dest='const_collection', const='value-2-to-append',
                    help='Add different values to list')
parser.add_argument('--version', action='version', version='%(prog)s 1.0')

print 'simple_value     =', args.simple_value
print 'constant_value   =', args.constant_value
print 'boolean_switch   =', args.boolean_switch
print 'collection       =', args.collection
print 'const_collection =', args.const_collection

'''
args = parser.parse_args()




print args.test
print str(type(args.test))


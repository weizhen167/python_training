import argparse,sys


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

# if we need to set a group of very complex
# the main idea of the argparse is to organize input arguments, to make them more readable and easy to use
# 02 parameters
#add help  parser.add_argument(dest = "echo", help = "echo the string you use here")
parser = argparse.ArgumentParser()
#"C:\Users\zwei\Anaconda2\python.exe" C:\Users\zwei\Desktop\args_parser_and_config_parser\args_parser.py

#parser.add_argument(dest ="test")
#parser.add_argument(dest = "test", help = "example of arg_parser")
#parser.add_argument(dest = "test", help = "example of arg_parser", type = int)
#parser.add_argument("-t", "--test",dest = "test", help = "example of arg_parser", type = int)
#parser.add_argument("-t", "--test",dest = "test", help = "example of arg_parser", choices=[0, 1, 2],type = int)
#parser.add_argument("-t", "--test",dest = "test", help = "example of arg_parser", choices=[0, 1, 2],type = int,required=True)
parser.add_argument("-t", "--test",dest = "test", help = "example of arg_parser", choices=[0, 1, 2],type = int,required=False,default=0)
args = parser.parse_args()
#a = args.test - 5
#print 'a is ' + str(a)
#print "value of 'test' is " + args.test



#03 actions
'''

parser.add_argument('-s', action='store', dest='simple_value',help='Store a simple value')
parser.add_argument('-c', action='store_const', dest='constant_value',const='sefas',
                    help='Store a constant value')
parser.add_argument('-t', action='store_true', default=False,dest='boolean_switch',
                    help='Set a switch to true')
parser.add_argument('-f', action='store_false', default=False,dest='boolean_switch',
                    help='Set a switch to false')



parser.add_argument('-a', action='append', dest='collection',default=[],help='Add repeated values to a list')
parser.add_argument('-A', action='append_const', dest='const_collection',const='sefasA',default=[],
                    help='Add different values to list')
parser.add_argument('-B', action='append_const', dest='const_collection', const='sefasB',
                    help='Add different values to list')
parser.add_argument('--version', action='version', version='%(prog)s 1.0')



print 'simple_value     =', args.simple_value
print 'constant_value   =', args.constant_value
print 'boolean_switch   =', args.boolean_switch
print 'collection       =', args.collection
print 'const_collection =', args.const_collection
'''






#print args.test
#print str(type(args.test))


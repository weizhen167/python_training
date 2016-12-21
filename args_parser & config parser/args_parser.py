import sys,argparse



parser = argparse.ArgumentParser()
#parser.add_argument("echo")
#args = parser.parse_args()


'''
#part1 intro
print "CMD is %s"  % (sys.argv)
print "length of args", len(sys.argv)
print "print each args"
for i, eachArg in enumerate(sys.argv):
    print "[%d] = %s" % (i, eachArg)
'''



'''
# set dest = "echo"
# our parser could read parameter "echo" from the input parameter
# after using parse_args() read parameter info, we can use args.echo to load that parameter
parser.add_argument(dest = "echo", help = "echo the string you use here")
args = parser.parse_args()

print "print all the parameter"
print "parameter", args
print "parameter types", type(args)

print "show string echo = ", args.echo   # use args.echo get parameter info
'''

#set a
'''
parser.add_argument(dest="m", help="enter the m...",type = int)
parser.add_argument(dest="n", help="enter the n...",type = int)
args = parser.parse_args()
m = args.m
n = args.n
print "%d ^ %d = %d" % (m, n, m ** n)


parser.add_argument("-m", "--m_number", dest = "m", help = "enter the m...", type = int)
parser.add_argument("-n", "--n_number", dest = "n", help = "enter the n...", type = int)
parser.add_argument("-w", "--w_number", dest = "w", help = "enter the w...")
args = parser.parse_args()
#print args.w
print "%d ^ %d = %d" % (args.m,  args.n, args.m ** args.n + args.w)
'''

parser = argparse.ArgumentParser(description='Example with long option names')

parser.add_argument('--noarg', action="store_true", default=False)
parser.add_argument('--witharg', action="store", dest="witharg")
parser.add_argument('--witharg2', action="store", dest="witharg2", type=int)

print parser.parse_args(['--noarg', '--witharg', 'val', '--witharg2=3'])




'''
if __name__ == "__main__":
    #part1 intro
    print "message has type %s, type %s"  % (sys.argv, len(sys.argv))
    print "length of args", len(sys.argv)
    print "print info of each args"
    for i, eachArg in enumerate(sys.argv):
        print "[%d] = %s" % (i, eachArg)
'''

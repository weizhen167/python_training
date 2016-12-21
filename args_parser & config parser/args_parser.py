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

parser.add_argument(dest="m", help="enter the m...")
parser.add_argument(dest="n", help="enter the n...")
args = parser.parse_args()
m_ = int(args.m)
n_ = int(args.n)
print "%d ^ %d = %d" % (m_, n_, m_ ** n_)

'''


if __name__ == "__main__":
    #part1 intro
    print "message has type %s, type %s"  % (sys.argv, len(sys.argv))
    print "length of args", len(sys.argv)
    print "print info of each args"
    for i, eachArg in enumerate(sys.argv):
        print "[%d] = %s" % (i, eachArg)

'''
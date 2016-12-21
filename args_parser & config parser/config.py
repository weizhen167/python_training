import ConfigParser

cf = ConfigParser.ConfigParser()
cf.read("config.ini")

# get all the sections from config
s = cf.sections()
print 'section:', s

# get the options of the given section. (load all keys)
o = cf.options("db")
print 'options:', o

# get the config info of the given section. (load all key,values pairs)
v = cf.items("db")
print 'db:', v

# read section option infomation according to it's type:
# for example: getfloat, getboolean.

# read as a int:
db_host = cf.get("db", "db_host")
db_port = cf.getint("db", "db_port")
db_user = cf.get("db", "db_user")
db_pass = cf.get("db", "db_pass")

#read as a int
threads = cf.getint("concurrent", "thread")
processors = cf.getint("concurrent", "processor")

print "db_host:", db_host, " type is: ", str(type(db_host))
print "db_port:", db_port, " type is: ",str(type(db_port))
print "db_user:", db_user, " type is: ",str(type(db_user))
print "db_pass:", db_pass, " type is: ",str(type(db_pass))
print "thread:", threads, " type is: ",str(type(threads))
print "processor:", processors, " type is: ",str(type(processors))


#set an option value.
cf.set("db", "db_pass", "sefas123")
cf.write(open("config.ini", "w")) ## remember to rewrite


#remove section or option
cf.remove_option('liuqing', 'int')
cf.remove_section('liuqing')
cf.write(open("config.ini", "w"))

#add a section
cf.add_section('liuqing')
cf.set('liuqing', 'int', '15')
cf.set('liuqing', 'bool', 'true')
cf.set('liuqing', 'float', '3.1415')
cf.set('liuqing', 'baz', 'fun')
cf.set('liuqing', 'bar', 'Python')
cf.set('liuqing', 'foo', '%(bar)s is %(baz)s!')
cf.write(open("config.ini", "w")) ## remember to rewrite


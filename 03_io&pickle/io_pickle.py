import pickle,pprint

#Reading from files

with open("test.txt", 'rb')as fd:
    #reader = fd.read()
    #reader = fd.readlines()
    #reader = fd.readline()
    #for line in fd:
     #   print line
    #content_read = fd.read(200)
    #print content_read
    block_size  = 200
    content_fd = fd.read(block_size)
    #while (len(content_fd) > 0):
     #   print content_fd
     #   content_fd = fd.read(block_size)
    print fd.tell()
    content_fd = fd.read()
    print fd.tell()
    fd.seek(0)
    print fd.tell()
    content_fd=fd.read(block_size)
    print content_fd
    #print reader

print 'fd closed??: ' + str(fd.closed)
#for line in reader:


#   print line


#Writing to files
# r+  read & write, w  write, a append
#with open('test2','w') as wf:
 #   wf.write('Writing to a new file')
  #  wf.seek(0)
   # wf.write('Writing  overwrite')

with open('Penguins.jpg', 'rb') as rf:
    with open('Penguins_copy.jpg', 'wb') as wf:
       for line in rf:
          wf.write(line)
    with open('Penguins_copy_2.jpg', 'wb') as wf2:
        chunk_size = 4096
        rf.seek(0)
        content_img = rf.read(chunk_size)
        while len(content_img)>0:
            wf2.write(content_img)
            content_img = rf.read(chunk_size)

#Creating pickle files

picklelist = ['one',2,'three','four',5,'can ypu count?']
pk = pickle.dumps(picklelist)
print pk

un_pk = pickle.loads(pk)
print un_pk

with open('list.pkl','wb') as wf:
    pickle.dump(picklelist,wf)

with open('list.pkl','rb') as rf:
    print pickle.load(rf)

with open('024211_premerged.pkl','rb') as rf:
    dict = pickle.load(rf)
    print pprint.pprint(dict)

#Accessing pickle files
"""


#json
import json
json_list = ['foo',{'batr0':('badsa',None,1.0,2)},{1:'test'}]
json_v = json.dumps(json_list)
print json.loads(json_v)
print json.dumps(dict)

"""
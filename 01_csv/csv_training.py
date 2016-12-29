import csv

# Exercise 1 : Simple Reader
print '********************Exercise 1********************'
fd = open('test_files/a.csv','r')
try:
    reader1 = csv.reader(fd)
    for row in reader1:
        print row;

except ValueError:
    print ValueError

finally:
    fd.close()
print ''
# Exercise 2a : Format keyword arguments

print '********************Exercise 2********************'
fd = open('test_files/b.csv','r')
try:
    reader1 = csv.reader(fd,skipinitialspace=True,quoting=csv.QUOTE_NONE)
    for row in reader1:
        print row;
except ValueError:
    print ValueError

finally:
    fd.close()

print ''
# Exercise 2b : Dialect
class MyDialect(csv.Dialect):
    skipinitialspace = True
    quoting = csv.QUOTE_NONE
    delimiter = ' '
    lineterminator =  '\n'

csv.register_dialect('my_dialect',MyDialect)
fd = open('test_files/b.csv','r')
try:
    reader1 = csv.reader(fd,dialect='my_dialect')
    for row in reader1:
        print row;
except ValueError:
    print ValueError
finally:
    fd.close()
print ''
print '********************Exercise 3********************'

# Exercise 3a : Index Reader

fd = open('test_files/c.ind','r')
try:
    reader1 = csv.reader(fd,delimiter='\t',
                         quoting=csv.QUOTE_NONE)
    for row in reader1:
        print row;

except ValueError:
    print ValueError

finally:
    fd.close()
print ''
# Exercise 3b : Index Writer
fd = open('test_files/c.ind','r')
fd_out = open('test_files/c_updates.ind','wb')
writer = csv.writer(fd_out, delimiter='\t',
                     quoting = csv.QUOTE_NONE)
try:
    reader1 = csv.reader(fd,delimiter='\t', quoting=csv.QUOTE_NONE)
    for row_num, row in enumerate(reader1):
        if row_num == 0:
            writer.writerow(row)
            continue
        row[-1] = 'usps'
        writer.writerow(row);
except ValueError:
    print ValueError
finally:
    fd.close()
    fd_out.close()
print ''


# Exercise 5 : DictReader
index_columns = [
    'OP_OFFSET',
    'MAILPIECE_ID',
    'ACCOUNT_NUMBER',
    'SHIP_TYPE'
]


fd = open('test_files/c.ind','r')
dictreader  =csv.DictReader(fd,index_columns,delimiter='\t', quoting=csv.QUOTE_NONE)


# Exercise 5b : DictWriter

fd_out = open('test_files/c_dict_updates.ind','wb')
dictwriter = csv.DictWriter(fd_out,index_columns,delimiter='\t', quoting=csv.QUOTE_NONE)
header =fd.readline()
print header
fd_out.write(header)

for row in dictreader:
    row['SHIP_TYPE'] = "USPS"
    dictwriter.writerow(row)

print row




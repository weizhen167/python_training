import csv

# Exercise 1 : Simple Reader
fd = open('test_files/a.csv','r')
try:
    reader1 = csv.reader(fd)
    for row in reader1:
        print row;

except ValueError:
    print ValueError

finally:
    fd.close()

# Exercise 2a : Format keyword arguments


# Exercise 2b : Dialect


# Exercise 3a : Index Reader

# Exercise 3b : Index Writer

# Exercise 5 : DictReader

# Exercise 5b : DictWriter

# Program to copy odd lines of one file to another
# open file in read mode
fn = open('nive.txt', 'r')

# open other file in write mode
fn1 = open('familyname', 'w')

# read the content of the file line by line
cont = fn.readlines()
type(cont) # list type
for i in range(1, len(cont)+1):
	if(i % 2 != 0):# check for odd line number
		fn1.write(cont[i-1])# write odd line to other file
	else:
		pass

# close the file
fn1.close()

# open file in read mode
fn1 = open('familyname', 'r')

# read the content of the file
cont1 = fn1.read()

# print the content of the file
print(cont1)

# close all files
fn.close()
fn1.close()



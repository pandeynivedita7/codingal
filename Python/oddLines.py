# Program to copy odd lines of one file to another

# open source file in read mode
fn = open('nive.txt', 'r')

# open destination file in write mode
fn1 = open('nive.txt', 'w')

# read the content of the file line by line
cont = fn.readlines()# read and readline

# copy only odd lines
for i in range(len(cont)):
    if i % 2 == 0:   # 0-based index → even index = odd line number
        fn1.write(cont[i])

# close the files
fn.close()
fn1.close()

# open updated file in read mode
fn1 = open('nive.txt', 'r')

# read the content of the file
cont1 = fn1.read()

# print the content of the file
print(cont1)

# close the updated file
fn1.close()

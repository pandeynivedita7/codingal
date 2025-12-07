# open the file in read mode
file_read = open('nive.txt', 'r')# variable name =open('file name','mode')
print("File in Read Mode -")
print(file_read.read())#read 2 types read() readline() readlines()
file_read.close()

# open the file in write mode
file_write = open('nive.txt', 'w')# r w a called as mode of file handling
# write in the file
file_write.write("File in write mode ....\n")
file_write.write("Hi! nivedita jeevika\n")
file_write.close()

# open the file in append mode
file_append = open('nive.txt', 'a')
# append in the file
file_append.write("\nFile in append mode ....\n")
file_append.write("Hi! jeevika is studying\n")
file_append.close()

# reopen file to check final content
file_final = open('nive.txt', 'r')
print("\nFinal File Contents -")
print(file_final.read())
file_final.close()

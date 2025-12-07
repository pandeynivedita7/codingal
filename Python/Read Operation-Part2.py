# open the file in read mode file operation txt
file_read = open('nive.txt', 'r')# 3 mode 1 write 2 read 3 append 
print("File in Read Mode -")
print(file_read.read(9))#read 2 types read() readline() readlines() 9 characters
file_read.close()

# open the file in write mode
file_write = open('nive.txt', 'w')
# write in the file
file_write.write("File in write mode ....\n")
file_write.write("Hi! I am Penguin. I am 1 yr. old\n")
file_write.close()

# open the file in append mode
file_append = open('nive.txt', 'a')
# append in the file
file_append.write("\nFile in append mode ....\n")
file_append.write("HI am jeevika\n")
file_append.close()

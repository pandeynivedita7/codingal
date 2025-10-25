import os

# create a new file
new_file = open('New_File.txt', 'x')
new_file.close()

# check if a file exists
print("Checking if my_file.txt exists or not....")
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
    print("my_file.txt deleted")
else:
    print("The file does not exist")

# create a new file if it doesn't exist
with open("my_file.txt", "w") as my_file:
    my_file.write("Hi! I am Penguin and I am 1 yr old.")

# delete file named Codingal.txt if it exists
if os.path.exists("Codingal.txt"):
    os.remove("Codingal.txt")
    print("Codingal.txt deleted")
else:
    print("Codingal.txt does not exist")

# delete the folder if it exists
if os.path.exists("Folder"):
    os.rmdir("Folder")
    print("Folder deleted")
else:
    print("Folder does not exist")

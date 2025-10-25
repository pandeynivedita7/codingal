# open file and read its contents
file = open('nive.txt', 'r')
print(file.read())
file.close()

# open file and read its beginning 8 characters
file = open('nive.txt', 'r')
print("\nRead in parts\n")
print(file.read(8))
file.close()

# append your name and age in the file
file = open('nive.txt', 'a')
file.write(" hi its jeevika i am 4 years old")
file.close()

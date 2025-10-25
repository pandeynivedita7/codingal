# write in file using with() function
with open('nive.txt', 'w') as file:
    file.write("Hi! I am Penguin and I am 1 yr old.")

# split file into words
with open('Codingal.txt', 'r') as file:
    data = file.readlines()
    print("Words in this file are....")
    for line in data:
        words = line.split()
        for word in words:
            print(word)

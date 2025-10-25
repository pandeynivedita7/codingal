# Take input of a word
string = input("Please enter your own word: ")#apple

# Take input of a character
char = input("Please enter your own character: ")#p

i = 0
count = 0

# Loop to find the occurrence of character 
while i < len(string):  # string operation count number of char in given word while condition true:
    if string[i] == char:  # apple == p
        count = count + 1
    i = i + 1

# Display the result
print("The total number of times", char, "has occurred =", count)

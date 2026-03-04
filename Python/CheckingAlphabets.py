# Program to check if a character is an alphabet

ch = input("Enter a character: ")

if len(ch) == 1 and ch.isalpha():# length count number of characters and isalpha() checks if the character is an alphabet
    print("The given character is an alphabet.")
else:
    print("The given character is NOT an alphabet.")
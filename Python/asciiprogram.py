# Ask the user to enter a character
char = input("Enter a character: ")

# Check if the input is a single character
if len(char) == 1:
    # Use ord() to get ASCII value
    ascii_value = ord(char)
    print("The ASCII value of is",ascii_value)
else:
    print("Please enter only a single character.")

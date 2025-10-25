# Ask user for input
user_input = input("Enter a string: ")
#. is used to call a method()
# Check if the string contains only alphabets
if user_input.isalpha():# string methods .lower().upper().len() validation .isalpha(alphabet) isnumeric(number)
    print("The string contains only alphabets.")

# Check if the string contains only digits
elif user_input.isnumeric():
    print("The string contains only numbers.")

# If it's a mix of characters
else:
    print("The string contains a mix of characters (not only alphabets or numbers).")

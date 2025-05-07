import random  # Import the 'random' module to generate random choices

# Print a message to let the user know the program has started
print("Starting password generator...")

# Define the set of characters that can be used in the password
characters = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

# Get the desired length of the password from the user input
password_length = int(input("Enter desired password length: "))

# Initialize an empty list to store password characters
password = []

# Loop through a range of numbers from 0 to the desired password length
for i in range(password_length):
    # Append a random character from 'characters' to the 'password' list
    password.append(random.choice(characters))

# Join all characters in the list into a single string
password = ''.join(password)

# Output the generated password
print("Your new password is: " + password)






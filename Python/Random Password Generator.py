import random# new random function
import string# string function

def generate_password(length=12):
    # characters to choose from: letters, digits, punctuation
    characters = string.ascii_letters + string.digits + string.punctuation# special symbol+_*&%$#
    # generate random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage
if __name__ == "__main__":# main function start
    length = int(input("Enter password length: "))
    print("Generated Password:", generate_password(length))
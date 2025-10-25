import random# random number 

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

print("Guess the number (between 1 and 10)")

# Ask the user for their guess
guess = int(input("Enter your guess: "))

# Check the guess
if guess == secret_number:#true
    print("🎉 Correct! You guessed the number!")
else:#false
    print(f"❌ Wrong! The number was {secret_number}")

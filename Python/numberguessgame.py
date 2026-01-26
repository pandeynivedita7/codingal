import random# random give you any random number 1,11

# Store numbers in a list
numbers = list(range(1, 11))  # Numbers 1 to 10
secret_number = random.choice(numbers)# randint(1, 10)

print("Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 10.")

while True:#condition 
    guess = int(input("Enter your guess: "))
    
    if guess == secret_number:#comparsion operator
        print("🎉 Congratulations! You guessed it right!")
        break#stop game
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

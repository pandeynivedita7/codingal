import random

options = ["Rock", "Paper", "Scissors"]# list [] which are collection of data mutable/changed tuple( collection of data but cant be change)

user_choice = input("Choose Rock, Paper, or Scissors: ")

computer_choice = random.choice(options)# randint/choice

print("You chose:", user_choice)
print("Computer chose:", computer_choice)

if user_choice == computer_choice:
    print("It's a tie!")# 3 logical operator and or not
elif user_choice == "Rock" and computer_choice == "Scissors":
    print("Rock smashes scissors! You win!")
elif user_choice == "Paper" and computer_choice == "Rock":
    print("Paper covers rock! You win!")
elif user_choice == "Scissors" and computer_choice == "Paper":
    print("Scissors cuts paper! You win!")
else:#false
    print("You lose!. ")

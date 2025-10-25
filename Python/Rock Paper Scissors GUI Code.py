import tkinter as tk
import random

# Function to handle the game logic
def play(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
        update_score("user")
    else:
        result = "Computer Wins!"
        update_score("computer")

    comp_label.config(text=f"Computer chose: {computer_choice}")
    result_label.config(text=result)


# Function to update score
def update_score(winner):
    global user_score, computer_score
    if winner == "user":
        user_score += 1
    elif winner == "computer":
        computer_score += 1
    score_label.config(text=f"Score → You: {user_score} | Computer: {computer_score}")


# Main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("350x300")

user_score = 0
computer_score = 0

# Title
tk.Label(root, text="Rock Paper Scissors", font=("Arial", 16, "bold")).pack(pady=10)

# Buttons for user choices
tk.Button(root, text="Rock", width=15, command=lambda: play("Rock")).pack(pady=5)
tk.Button(root, text="Paper", width=15, command=lambda: play("Paper")).pack(pady=5)
tk.Button(root, text="Scissors", width=15, command=lambda: play("Scissors")).pack(pady=5)

# Labels for output
comp_label = tk.Label(root, text="Computer chose: ", font=("Arial", 12))
comp_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score → You: 0 | Computer: 0", font=("Arial", 12))
score_label.pack(pady=10)

# Exit button
tk.Button(root, text="Quit Game", width=15, command=root.quit, bg="red", fg="white").pack(pady=10)

root.mainloop()

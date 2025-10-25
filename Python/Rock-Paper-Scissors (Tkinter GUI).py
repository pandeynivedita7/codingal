import tkinter as tk
import random

# Game options
choices = ["Rock", "Paper", "Scissors"]

# Scores
user_score = 0
comp_score = 0

def play(user_choice):
    global user_score, comp_score

    # Computer makes a choice
    comp_choice = random.choice(choices)

    # Determine winner
    if user_choice == comp_choice:
        result = "It's a Draw!"
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Paper" and comp_choice == "Rock") or \
         (user_choice == "Scissors" and comp_choice == "Paper"):
        result = "You Win!"
        user_score += 1
    else:
        result = "Computer Wins!"
        comp_score += 1

    # Update labels
    user_label.config(text=f"Your Choice: {user_choice}")
    comp_label.config(text=f"Computer's Choice: {comp_choice}")
    result_label.config(text=result)
    score_label.config(text=f"Score → You: {user_score} | Computer: {comp_score}")

# Reset game
def reset_game():
    global user_score, comp_score
    user_score = 0
    comp_score = 0
    user_label.config(text="Your Choice: ")
    comp_label.config(text="Computer's Choice: ")
    result_label.config(text="Result will be shown here")
    score_label.config(text="Score → You: 0 | Computer: 0")

# Main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x400")
root.resizable(False, False)

# Title
title = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold"))
title.pack(pady=10)

# Labels
user_label = tk.Label(root, text="Your Choice: ", font=("Arial", 14))
user_label.pack()
comp_label = tk.Label(root, text="Computer's Choice: ", font=("Arial", 14))
comp_label.pack()
result_label = tk.Label(root, text="Result will be shown here", font=("Arial", 14, "bold"), fg="blue")
result_label.pack(pady=10)
score_label = tk.Label(root, text="Score → You: 0 | Computer: 0", font=("Arial", 14, "bold"))
score_label.pack(pady=10)

# Buttons for choices
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

rock_btn = tk.Button(button_frame, text="Rock", width=10, height=2, command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(button_frame, text="Paper", width=10, height=2, command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(button_frame, text="Scissors", width=10, height=2, command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

# Reset button
reset_btn = tk.Button(root, text="Reset Game", width=15, height=2, bg="tomato", command=reset_game)
reset_btn.pack(pady=15)

root.mainloop()

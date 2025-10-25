import tkinter as tk
from tkinter import messagebox

# Initialize main window
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("320x350")

# Player symbols
current_player = "X"
board = [""] * 9  # 3x3 board stored as list

# Function to check winner
def check_winner():
    global current_player
    win_combinations = [
        (0,1,2), (3,4,5), (6,7,8),  # rows
        (0,3,6), (1,4,7), (2,5,8),  # cols
        (0,4,8), (2,4,6)             # diagonals
    ]
    for a, b, c in win_combinations:
        if board[a] == board[b] == board[c] != "":
            messagebox.showinfo("Game Over", f"Player {board[a]} Wins!")
            reset_game()
            return True
    if "" not in board:
        messagebox.showinfo("Game Over", "It's a Tie!")
        reset_game()
        return True
    return False

# Function to handle button click
def on_click(index):
    global current_player
    if board[index] == "":
        board[index] = current_player
        buttons[index].config(text=current_player, state="disabled")
        
        if not check_winner():
            current_player = "O" if current_player == "X" else "X"
            turn_label.config(text=f"Player {current_player}'s Turn")

# Function to reset the game
def reset_game():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    for btn in buttons:
        btn.config(text="", state="normal")
    turn_label.config(text="Player X's Turn")

# Title
tk.Label(root, text="Tic Tac Toe", font=("Arial", 16, "bold")).pack(pady=10)

# Turn label
turn_label = tk.Label(root, text="Player X's Turn", font=("Arial", 12))
turn_label.pack(pady=5)

# Frame for buttons
frame = tk.Frame(root)
frame.pack()

# Create 9 buttons for the board
buttons = []
for i in range(9):
    btn = tk.Button(frame, text="", width=8, height=3, font=("Arial", 14),
                    command=lambda i=i: on_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

# Reset button
tk.Button(root, text="Reset Game", command=reset_game, bg="blue", fg="white").pack(pady=10)

# Exit button
tk.Button(root, text="Quit", command=root.quit, bg="red", fg="white").pack()

root.mainloop()

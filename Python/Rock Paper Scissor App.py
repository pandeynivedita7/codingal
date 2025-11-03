import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors Game")
        self.root.geometry("600x700")
        self.root.resizable(False, False)
        self.root.configure(bg='#1a1a2e')
        
        # Game variables
        self.user_score = 0
        self.computer_score = 0
        self.ties = 0
        self.choices = ['Rock', 'Paper', 'Scissors']
        
        # Emojis for choices
        self.choice_emojis = {
            'Rock': '🪨',
            'Paper': '📄',
            'Scissors': '✂️'
        }
        
        self.setup_ui()
    
    def setup_ui(self):
        # Title
        title_label = tk.Label(
            self.root,
            text="Rock Paper Scissors",
            font=("Arial", 28, "bold"),
            bg='#1a1a2e',
            fg='#00d9ff'
        )
        title_label.pack(pady=20)
        
        # Score frame
        score_frame = tk.Frame(self.root, bg='#16213e', relief=tk.RAISED, borderwidth=3)
        score_frame.pack(pady=10, padx=20, fill='x')
        
        tk.Label(
            score_frame,
            text="SCOREBOARD",
            font=("Arial", 14, "bold"),
            bg='#16213e',
            fg='#00d9ff'
        ).pack(pady=10)
        
        scores_container = tk.Frame(score_frame, bg='#16213e')
        scores_container.pack(pady=10)
        
        # User score
        tk.Label(
            scores_container,
            text="You",
            font=("Arial", 12, "bold"),
            bg='#16213e',
            fg='#4ecca3'
        ).grid(row=0, column=0, padx=30)
        
        self.user_score_label = tk.Label(
            scores_container,
            text="0",
            font=("Arial", 24, "bold"),
            bg='#16213e',
            fg='#4ecca3'
        )
        self.user_score_label.grid(row=1, column=0, padx=30)
        
        # Ties
        tk.Label(
            scores_container,
            text="Ties",
            font=("Arial", 12, "bold"),
            bg='#16213e',
            fg='#ffd700'
        ).grid(row=0, column=1, padx=30)
        
        self.ties_label = tk.Label(
            scores_container,
            text="0",
            font=("Arial", 24, "bold"),
            bg='#16213e',
            fg='#ffd700'
        )
        self.ties_label.grid(row=1, column=1, padx=30)
        
        # Computer score
        tk.Label(
            scores_container,
            text="Computer",
            font=("Arial", 12, "bold"),
            bg='#16213e',
            fg='#ff6b6b'
        ).grid(row=0, column=2, padx=30)
        
        self.computer_score_label = tk.Label(
            scores_container,
            text="0",
            font=("Arial", 24, "bold"),
            bg='#16213e',
            fg='#ff6b6b'
        )
        self.computer_score_label.grid(row=1, column=2, padx=30)
        
        # Game result display
        self.result_frame = tk.Frame(self.root, bg='#0f3460', relief=tk.RAISED, borderwidth=3)
        self.result_frame.pack(pady=20, padx=20, fill='both', expand=True)
        
        tk.Label(
            self.result_frame,
            text="Make Your Choice!",
            font=("Arial", 16, "bold"),
            bg='#0f3460',
            fg='#ffffff'
        ).pack(pady=20)
        
        # Choice display frame
        choice_display = tk.Frame(self.result_frame, bg='#0f3460')
        choice_display.pack(pady=10)
        
        # User choice display
        user_choice_frame = tk.Frame(choice_display, bg='#0f3460')
        user_choice_frame.pack(side='left', padx=30)
        
        tk.Label(
            user_choice_frame,
            text="You",
            font=("Arial", 12, "bold"),
            bg='#0f3460',
            fg='#4ecca3'
        ).pack()
        
        self.user_choice_label = tk.Label(
            user_choice_frame,
            text="?",
            font=("Arial", 48),
            bg='#0f3460',
            fg='#ffffff'
        )
        self.user_choice_label.pack(pady=10)
        
        # VS label
        tk.Label(
            choice_display,
            text="VS",
            font=("Arial", 20, "bold"),
            bg='#0f3460',
            fg='#ffd700'
        ).pack(side='left', padx=20)
        
        # Computer choice display
        computer_choice_frame = tk.Frame(choice_display, bg='#0f3460')
        computer_choice_frame.pack(side='left', padx=30)
        
        tk.Label(
            computer_choice_frame,
            text="Computer",
            font=("Arial", 12, "bold"),
            bg='#0f3460',
            fg='#ff6b6b'
        ).pack()
        
        self.computer_choice_label = tk.Label(
            computer_choice_frame,
            text="?",
            font=("Arial", 48),
            bg='#0f3460',
            fg='#ffffff'
        )
        self.computer_choice_label.pack(pady=10)
        
        # Result message
        self.result_message = tk.Label(
            self.result_frame,
            text="",
            font=("Arial", 18, "bold"),
            bg='#0f3460',
            fg='#ffd700'
        )
        self.result_message.pack(pady=20)
        
        # Buttons frame
        button_frame = tk.Frame(self.root, bg='#1a1a2e')
        button_frame.pack(pady=20)
        
        # Rock button
        rock_btn = tk.Button(
            button_frame,
            text="🪨\nRock",
            font=("Arial", 14, "bold"),
            bg='#4ecca3',
            fg='#1a1a2e',
            activebackground='#3db88f',
            width=10,
            height=4,
            command=lambda: self.play('Rock'),
            cursor='hand2'
        )
        rock_btn.grid(row=0, column=0, padx=10)
        
        # Paper button
        paper_btn = tk.Button(
            button_frame,
            text="📄\nPaper",
            font=("Arial", 14, "bold"),
            bg='#4ecca3',
            fg='#1a1a2e',
            activebackground='#3db88f',
            width=10,
            height=4,
            command=lambda: self.play('Paper'),
            cursor='hand2'
        )
        paper_btn.grid(row=0, column=1, padx=10)
        
        # Scissors button
        scissors_btn = tk.Button(
            button_frame,
            text="✂️\nScissors",
            font=("Arial", 14, "bold"),
            bg='#4ecca3',
            fg='#1a1a2e',
            activebackground='#3db88f',
            width=10,
            height=4,
            command=lambda: self.play('Scissors'),
            cursor='hand2'
        )
        scissors_btn.grid(row=0, column=2, padx=10)
        
        # Reset button
        reset_btn = tk.Button(
            self.root,
            text="Reset Game",
            font=("Arial", 12, "bold"),
            bg='#ff6b6b',
            fg='#ffffff',
            activebackground='#ee5a52',
            command=self.reset_game,
            cursor='hand2',
            padx=20,
            pady=10
        )
        reset_btn.pack(pady=10)
    
    def play(self, user_choice):
        # Computer makes random choice
        computer_choice = random.choice(self.choices)
        
        # Display choices
        self.user_choice_label.config(text=self.choice_emojis[user_choice])
        self.computer_choice_label.config(text=self.choice_emojis[computer_choice])
        
        # Determine winner
        result = self.determine_winner(user_choice, computer_choice)
        
        # Update scores
        if result == 'win':
            self.user_score += 1
            self.result_message.config(text="🎉 You Win! 🎉", fg='#4ecca3')
        elif result == 'lose':
            self.computer_score += 1
            self.result_message.config(text="😢 You Lose! 😢", fg='#ff6b6b')
        else:
            self.ties += 1
            self.result_message.config(text="🤝 It's a Tie! 🤝", fg='#ffd700')
        
        # Update score labels
        self.user_score_label.config(text=str(self.user_score))
        self.computer_score_label.config(text=str(self.computer_score))
        self.ties_label.config(text=str(self.ties))
    
    def determine_winner(self, user, computer):
        if user == computer:
            return 'tie'
        
        winning_combinations = {
            'Rock': 'Scissors',
            'Paper': 'Rock',
            'Scissors': 'Paper'
        }
        
        if winning_combinations[user] == computer:
            return 'win'
        else:
            return 'lose'
    
    def reset_game(self):
        # Reset scores
        self.user_score = 0
        self.computer_score = 0
        self.ties = 0
        
        # Reset labels
        self.user_score_label.config(text="0")
        self.computer_score_label.config(text="0")
        self.ties_label.config(text="0")
        self.user_choice_label.config(text="?")
        self.computer_choice_label.config(text="?")
        self.result_message.config(text="")


if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
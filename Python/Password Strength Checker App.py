from tkinter import *
from tkinter import messagebox
import re# regular expression module for pattern matching s%cenarios

class PasswordStrengthChecker:
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x550")
        self.root.title("Password Strength Checker")
        self.root.config(bg="#f0f0f0")

        # Title Label
        title_label = Label(root, text="Password Strength Checker",
                           font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#333333")
        title_label.pack(pady=20)

        # Password Input Frame
        input_frame = Frame(root, bg="#f0f0f0")
        input_frame.pack(pady=15)

        Label(input_frame, text="Enter Password:", font=("Arial", 12, "bold"),
              bg="#f0f0f0").pack(anchor=W, padx=20)

        self.password_entry = Entry(input_frame, font=("Arial", 12), width=35, show="●")
        self.password_entry.pack(padx=20, pady=5)
        self.password_entry.bind("<KeyRelease>", self.check_strength)
        # Bind key release event for real-time checking (<event> calling function)
        # Strength Meter Frame
        meter_frame = Frame(root, bg="#f0f0f0")
        meter_frame.pack(pady=20)

        Label(meter_frame, text="Strength Level:", font=("Arial", 11, "bold"),
              bg="#f0f0f0").pack(anchor=W, padx=20)

        self.strength_bar = Frame(meter_frame, bg="#e0e0e0", height=20, width=300)
        self.strength_bar.pack(padx=20, pady=10, fill=X)

        # Strength Label
        self.strength_label = Label(root, text="Strength: Very Weak", font=("Arial", 12, "bold"),
                                   bg="#f0f0f0", fg="#d32f2f")
        self.strength_label.pack(pady=10)

        # Criteria Frame
        criteria_frame = Frame(root, bg="white", relief=SUNKEN, bd=2)
        criteria_frame.pack(pady=15, padx=20, fill=BOTH, expand=True)

        Label(criteria_frame, text="Password Criteria:", font=("Arial", 11, "bold"),
              bg="white").pack(anchor=NW, padx=10, pady=10)

        self.criteria_text = Text(criteria_frame, font=("Arial", 10), height=8, width=50)
        self.criteria_text.pack(padx=10, pady=10, fill=BOTH, expand=True)
        self.criteria_text.config(state=DISABLED)

        # Buttons Frame
        button_frame = Frame(root, bg="#f0f0f0")
        button_frame.pack(pady=15)

        check_button = Button(button_frame, text="Check Strength", font=("Arial", 11, "bold"),
                             bg="#4CAF50", fg="white", command=self.display_strength, padx=15, pady=8)
        check_button.pack(side=LEFT, padx=10)

        reset_button = Button(button_frame, text="Reset", font=("Arial", 11, "bold"),
                             bg="#f44336", fg="white", command=self.reset, padx=15, pady=8)
        reset_button.pack(side=LEFT, padx=10)

    def calculate_strength(self, password):
        """Calculate password strength score"""
        score = 0
        feedback = []

        # Length criteria
        if len(password) >= 8:
            score += 1
            feedback.append("✓ Length is at least 8 characters")
        else:
            feedback.append("✗ Length should be at least 8 characters")

        if len(password) >= 12:
            score += 1
            feedback.append("✓ Length is at least 12 characters")

        if len(password) >= 16:
            score += 1
            feedback.append("✓ Length is 16 or more characters")

        # Uppercase letters
        if re.search(r"[A-Z]", password):
            score += 1
            feedback.append("✓ Contains uppercase letters")
        else:
            feedback.append("✗ Add uppercase letters (A-Z)")

        # Lowercase letters
        if re.search(r"[a-z]", password):
            score += 1
            feedback.append("✓ Contains lowercase letters")
        else:
            feedback.append("✗ Add lowercase letters (a-z)")

        # Numbers
        if re.search(r"\d", password):
            score += 1
            feedback.append("✓ Contains numbers")
        else:
            feedback.append("✗ Add numbers (0-9)")

        # Special characters
        if re.search(r"[!@#$%^&*()_+\-=\[\]{};:'\",.<>?/\\|`~]", password):
            score += 1
            feedback.append("✓ Contains special characters")
        else:
            feedback.append("✗ Add special characters (!@#$%^&*)")

        return score, feedback

    def get_strength_level(self, score):
        """Determine strength level and color"""
        if score <= 1:
            return "Very Weak", "#d32f2f", 10
        elif score == 2:
            return "Weak", "#f57c00", 40
        elif score == 3:
            return "Fair", "#fbc02d", 60
        elif score == 4:
            return "Good", "#7cb342", 75
        elif score == 5:
            return "Strong", "#388e3c", 85
        else:
            return "Very Strong", "#1b5e20", 100

    def check_strength(self, event=None):
        """Real-time password strength checking"""
        password = self.password_entry.get()

        if password:
            score, feedback = self.calculate_strength(password)
            strength, color, percentage = self.get_strength_level(score)

            # Update strength label
            self.strength_label.config(text=f"Strength: {strength}", fg=color)

            # Update strength bar
            bar_width = int(300 * percentage / 100)
            self.strength_bar.config(bg=color)

            # Update criteria
            self.criteria_text.config(state=NORMAL)
            self.criteria_text.delete(1.0, END)
            criteria_display = "\n".join(feedback)
            self.criteria_text.insert(1.0, criteria_display)
            self.criteria_text.config(state=DISABLED)
        else:
            self.strength_label.config(text="Strength: Very Weak", fg="#d32f2f")
            self.strength_bar.config(bg="#e0e0e0")
            self.criteria_text.config(state=NORMAL)
            self.criteria_text.delete(1.0, END)
            self.criteria_text.config(state=DISABLED)

    def display_strength(self):
        """Display full strength report"""
        password = self.password_entry.get()

        if not password:
            messagebox.showwarning("Warning", "Please enter a password!")
            return

        score, feedback = self.calculate_strength(password)
        strength, color, percentage = self.get_strength_level(score)

        report = f"Password Strength Report\n"
        report += "=" * 40 + "\n\n"
        report += f"Overall Strength: {strength}\n"
        report += f"Score: {score}/7\n\n"
        report += "Details:\n"
        report += "\n".join(feedback)

        messagebox.showinfo("Password Strength Report", report)

    def reset(self):
        """Reset all fields"""
        self.password_entry.delete(0, END)
        self.strength_label.config(text="Strength: Very Weak", fg="#d32f2f")
        self.strength_bar.config(bg="#e0e0e0")
        self.criteria_text.config(state=NORMAL)
        self.criteria_text.delete(1.0, END)
        self.criteria_text.config(state=DISABLED)
        self.password_entry.focus()

# Create main window
root = Tk()
app = PasswordStrengthChecker(root)
root.mainloop()
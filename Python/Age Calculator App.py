import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class AgeCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Age Calculator")
        self.root.geometry("400x450")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")
        
        # Title
        title_label = tk.Label(
            root,
            text="Age Calculator",
            font=("Arial", 24, "bold"),
            bg="#f0f0f0",
            fg="#333"
        )
        title_label.pack(pady=20)
        
        # Frame for input fields
        input_frame = tk.Frame(root, bg="#f0f0f0")
        input_frame.pack(pady=10)
        
        # Day input
        tk.Label(
            input_frame,
            text="Day:",
            font=("Arial", 12),
            bg="#f0f0f0"
        ).grid(row=0, column=0, padx=10, pady=10, sticky="e")
        
        self.day_var = tk.StringVar()
        day_spinbox = tk.Spinbox(
            input_frame,
            from_=1,
            to=31,
            textvariable=self.day_var,
            font=("Arial", 12),
            width=15
        )
        day_spinbox.grid(row=0, column=1, padx=10, pady=10)
        
        # Month input
        tk.Label(
            input_frame,
            text="Month:",
            font=("Arial", 12),
            bg="#f0f0f0"
        ).grid(row=1, column=0, padx=10, pady=10, sticky="e")
        
        self.month_var = tk.StringVar()
        month_combo = ttk.Combobox(
            input_frame,
            textvariable=self.month_var,
            font=("Arial", 12),
            width=13,
            state="readonly"
        )
        month_combo['values'] = (
            'January', 'February', 'March', 'April', 'May', 'June',
            'July', 'August', 'September', 'October', 'November', 'December'
        )
        month_combo.grid(row=1, column=1, padx=10, pady=10)
        
        # Year input
        tk.Label(
            input_frame,
            text="Year:",
            font=("Arial", 12),
            bg="#f0f0f0"
        ).grid(row=2, column=0, padx=10, pady=10, sticky="e")
        
        self.year_var = tk.StringVar()
        year_spinbox = tk.Spinbox(
            input_frame,
            from_=1900,
            to=datetime.now().year,
            textvariable=self.year_var,
            font=("Arial", 12),
            width=15
        )
        year_spinbox.grid(row=2, column=1, padx=10, pady=10)
        
        # Calculate button
        calc_button = tk.Button(
            root,
            text="Calculate Age",
            font=("Arial", 14, "bold"),
            bg="#4CAF50",
            fg="white",
            cursor="hand2",
            command=self.calculate_age,
            relief=tk.RAISED,
            bd=3
        )
        calc_button.pack(pady=20)
        
        # Result frame
        result_frame = tk.Frame(root, bg="white", relief=tk.GROOVE, bd=2)
        result_frame.pack(pady=10, padx=30, fill="both")
        
        tk.Label(
            result_frame,
            text="Your Age:",
            font=("Arial", 14, "bold"),
            bg="white",
            fg="#333"
        ).pack(pady=10)
        
        self.result_label = tk.Label(
            result_frame,
            text="--",
            font=("Arial", 18),
            bg="white",
            fg="#4CAF50"
        )
        self.result_label.pack(pady=10, padx=20)
        
    def calculate_age(self):
        try:
            # Get input values
            day = int(self.day_var.get())
            month_name = self.month_var.get()
            year = int(self.year_var.get())
            
            # Validate inputs
            if not month_name:
                messagebox.showerror("Error", "Please select a month!")
                return
            
            # Convert month name to number
            months = {
                'January': 1, 'February': 2, 'March': 3, 'April': 4,
                'May': 5, 'June': 6, 'July': 7, 'August': 8,
                'September': 9, 'October': 10, 'November': 11, 'December': 12
            }
            month = months[month_name]
            
            # Create birth date
            birth_date = datetime(year, month, day)
            today = datetime.now()
            
            # Check if birth date is in the future
            if birth_date > today:
                messagebox.showerror("Error", "Birth date cannot be in the future!")
                return
            
            # Calculate age
            age_years = today.year - birth_date.year
            age_months = today.month - birth_date.month
            age_days = today.day - birth_date.day
            
            # Adjust for negative days
            if age_days < 0:
                age_months -= 1
                # Get days in previous month
                prev_month = today.month - 1 if today.month > 1 else 12
                prev_year = today.year if today.month > 1 else today.year - 1
                days_in_prev_month = (datetime(prev_year, prev_month + 1, 1) - 
                                     datetime(prev_year, prev_month, 1)).days
                age_days += days_in_prev_month
            
            # Adjust for negative months
            if age_months < 0:
                age_years -= 1
                age_months += 12
            
            # Display result
            result_text = f"{age_years} years, {age_months} months, {age_days} days"
            self.result_label.config(text=result_text)
            
        except ValueError as e:
            messagebox.showerror("Error", "Invalid date! Please check your input.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create and run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = AgeCalculator(root)
    root.mainloop()
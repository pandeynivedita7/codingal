import tkinter as tk
from datetime import datetime
from tkinter import messagebox

def calculate_age():
    try:
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())
        
        birth_date = datetime(year, month, day)
        today = datetime.now()
        
        if birth_date > today:
            messagebox.showerror("Error", "Birth date cannot be in the future!")
            return
        
        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
        
        result_label.config(text=f"Your age is: {age} years")
        
    except:
        messagebox.showerror("Error", "Please enter a valid date!")

# Create window
root = tk.Tk()
root.title("Age Calculator")
root.geometry("300x250")

# Title
tk.Label(root, text="Age Calculator", font=("Arial", 16, "bold")).pack(pady=10)

# Input fields
tk.Label(root, text="Day:").pack()
day_entry = tk.Entry(root, width=20)
day_entry.pack(pady=5)

tk.Label(root, text="Month:").pack()
month_entry = tk.Entry(root, width=20)
month_entry.pack(pady=5)

tk.Label(root, text="Year:").pack()
year_entry = tk.Entry(root, width=20)
year_entry.pack(pady=5)

# Calculate button
tk.Button(root, text="Calculate", command=calculate_age, bg="lightblue").pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
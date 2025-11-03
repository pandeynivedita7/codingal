import tkinter as tk
from datetime import datetime

def calculate_age():
    # Get values from entries
    day = day_entry.get()
    month = month_entry.get()
    year = year_entry.get()
    
    print(f"Day: {day}, Month: {month}, Year: {year}")  # Debug print
    
    try:
        # Convert to integers
        day = int(day)
        month = int(month)
        year = int(year)
        
        # Create birth date
        birth_date = datetime(year, month, day)
        today = datetime.now()
        
        # Calculate age
        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
        
        # Display result
        result_label.config(text=f"Your age is: {age} years")
        print(f"Age calculated: {age}")  # Debug print
        
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}")
        print(f"Error: {e}")  # Debug print

# Create main window
root = tk.Tk()
root.title("Age Calculator")
root.geometry("350x300")
root.configure(bg="white")

# Title
title = tk.Label(root, text="Age Calculator", font=("Arial", 18, "bold"), bg="white")
title.pack(pady=15)

# Day input
tk.Label(root, text="Enter Day (1-31):", bg="white", font=("Arial", 10)).pack()
day_entry = tk.Entry(root, width=25, font=("Arial", 11))
day_entry.pack(pady=5)
day_entry.insert(0, "15")

# Month input
tk.Label(root, text="Enter Month (1-12):", bg="white", font=("Arial", 10)).pack()
month_entry = tk.Entry(root, width=25, font=("Arial", 11))
month_entry.pack(pady=5)
month_entry.insert(0, "6")

# Year input
tk.Label(root, text="Enter Year (e.g., 1990):", bg="white", font=("Arial", 10)).pack()
year_entry = tk.Entry(root, width=25, font=("Arial", 11))
year_entry.pack(pady=5)
year_entry.insert(0, "2000")

# Calculate button
calc_btn = tk.Button(root, text="Calculate Age", command=calculate_age, 
                     bg="lightblue", font=("Arial", 12, "bold"), 
                     width=15)
calc_btn.pack(pady=15)

# Result label
result_label = tk.Label(root, text="Click Calculate to see your age", 
                       font=("Arial", 12), bg="white", fg="blue")
result_label.pack(pady=10)

print("Program started")  # Debug print

# Start the application
root.mainloop()
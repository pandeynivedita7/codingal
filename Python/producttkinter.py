import tkinter as tk
from tkinter import messagebox

def calculate_product():
    try:
        # Get user input
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        # Calculate product
        product = num1 * num2

        # Display result
        result_label.config(text=f"Product: {product}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

# Create main window
root = tk.Tk()
root.title("Product Calculator")
root.geometry("300x200")

# Labels and Entry fields
label1 = tk.Label(root, text="Enter first number:")
label1.pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

label2 = tk.Label(root, text="Enter second number:")
label2.pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

# Button to calculate product
calc_button = tk.Button(root, text="Calculate Product", command=calculate_product)
calc_button.pack(pady=10)

# Label to display result
result_label = tk.Label(root, text="Product: ")
result_label.pack(pady=5)

# Run the application
root.mainloop()

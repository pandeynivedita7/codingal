import tkinter as tk

def convert_length():
    try:
        inches = float(entry_inch.get())
        centimeters = inches * 2.54
        result_label.config(text=f"{centimeters:.2f} cm")
    except ValueError:
        result_label.config(text="Enter a valid number")

# main window
root = tk.Tk()
root.title("Length Converter - Inches to Centimeters")
root.geometry("300x150")

# widgets
tk.Label(root, text="Enter length in inches:").pack(pady=5)
entry_inch = tk.Entry(root)
entry_inch.pack(pady=5)

tk.Button(root, text="Convert", command=convert_length).pack(pady=5)
result_label = tk.Label(root, text="")
result_label.pack(pady=5)

root.mainloop()

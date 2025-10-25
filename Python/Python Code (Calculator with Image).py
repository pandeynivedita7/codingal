import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Function to evaluate the expression
def press(key):
    entry_text.set(entry_text.get() + str(key))

def clear():
    entry_text.set("")

def backspace():
    current_text = entry_text.get()
    entry_text.set(current_text[:-1])

def evaluate():
    try:
        result = str(eval(entry_text.get()))
        entry_text.set(result)
    except:
        messagebox.showerror("Error", "Invalid Expression")

# Create main window
root = tk.Tk()
root.title("Calculator with Image")
root.geometry("350x550")
root.resizable(False, False)

# Load and place image (change 'app_img.jpg' to your image file)
try:
    img = Image.open("calculatorimage.jpg")  # Make sure this file is in the same folder
    img = img.resize((120, 120))  # Resize image
    photo = ImageTk.PhotoImage(img)
    img_label = tk.Label(root, image=photo)
    img_label.pack(pady=10)
except:
    tk.Label(root, text="Image not found", font=("Arial", 12), fg="red").pack(pady=10)

# Entry widget
entry_text = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_text, font=("Arial", 20), bd=10, relief="ridge", justify="right")
entry.pack(fill="both", ipadx=8, ipady=15, pady=10)

# Button Frame
frame = tk.Frame(root)
frame.pack()

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

# Create buttons
for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(frame, text=text, width=5, height=2, font=("Arial", 18),
                        command=evaluate, bg="lightgreen")
    else:
        btn = tk.Button(frame, text=text, width=5, height=2, font=("Arial", 18),
                        command=lambda key=text: press(key))
    btn.grid(row=row, column=col, padx=5, pady=5)

# Extra Buttons
tk.Button(frame, text="C", width=5, height=2, font=("Arial", 18), command=clear, bg="tomato").grid(row=5, column=0, padx=5, pady=5)
tk.Button(frame, text="⌫", width=5, height=2, font=("Arial", 18), command=backspace, bg="lightblue").grid(row=5, column=1, padx=5, pady=5)

root.mainloop()

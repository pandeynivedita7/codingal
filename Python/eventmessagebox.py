import tkinter as tk

def change_color(event):
    # event.widget gives which button triggered the event
    color = event.widget["text"]
    label.config(text=f"Color changed to {color}", bg=color.lower())

# main window
root = tk.Tk()
root.title("Event Handling Example - Color Changer")
root.geometry("400x300")

# label
label = tk.Label(root, text="Click a button to change my color!", font=("Arial", 14))
label.pack(pady=30)

# buttons
colors = ["Red", "Green", "Blue"]
for color in colors:
    btn = tk.Button(root, text=color, width=10, height=2)
    btn.pack(pady=5)
    # Bind left mouse click (Button-1) event to function
    btn.bind("<Button-1>", change_color)

root.mainloop()
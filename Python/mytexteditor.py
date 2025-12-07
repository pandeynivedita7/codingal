# Import necessary packages
from tkinter import *# * imports all classes and functions from tkinter.
from tkinter.filedialog import askopenfilename, asksaveasfilename# Import file dialog functions for opening and saving files.

# Setup Root Window
window = Tk()# Create the main application window.
window.title("Nivedita Text Editor")
window.geometry("600x500")# width x height
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)#lets the widgets expand when the window is resized.

# Function to Open a file
def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, END)#Clears the text editor before loading new content.
    with open(filepath, "r") as input_file:# file open varname=open(filename, mode) r w a
        text = input_file.read()
        txt_edit.insert(END, text)
    window.title(f"Nivedita Text Editor - {filepath}")

# Function to Save a file
def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, END)#Reads text from editor (get(1.0, END)) and writes it to the file.
        output_file.write(text)
    window.title(f"Codingal's Text Editor - {filepath}")

# Add widgets in the application
txt_edit = Text(window)
fr_buttons = Frame(window, relief=RAISED, bd=2)
btn_open = Button(fr_buttons, text="Open", command=open_file)
btn_save = Button(fr_buttons, text="Save As...", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)#sticky defines how widgets stretch (n = north, s = south, e = east, w = west).
btn_save.grid(row=1, column=0, sticky="ew", padx=5, pady=5)#add space around widgets.padxy used to add space around widgets.

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

# Start the GUI event loop
window.mainloop()

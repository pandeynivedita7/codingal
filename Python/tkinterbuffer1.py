# Import necessary libraries
from tkinter import *

# Create Window
root = Tk()
root.title('Getting Started with Widgets')
root.geometry('400x300')

# Add widgets
# Add Label 
lbl1 = Label(text = "Full Name", bg="#3895D3", fg='white')
lbl2 = Label(text = "Email Id", bg="#3895D3", fg='white')
lbl3 = Label(text = "Enter Password", bg="#3895D3", fg='white')

# Use Entry Widget to create a text box for user to enter details
name_entry = Entry()
email_entry = Entry()
pass_entry = Entry(show="*")

# Function to display message
def display():
	name = name_entry.get()
	greet = "Hey "+name
	message =  "\nCongratulations for your new account!"
	textbox.insert(END, greet)
	textbox.insert(END, message)

# Textbox to display message
textbox = Text(bg="#BEBEBE", fg="black")

# Add Button, when pressed, message will be displayed
btn = Button(text = "Create Account", command=display)

# Arrange all widgets
lbl1.pack()
name_entry.pack()
lbl2.pack()
email_entry.pack()
lbl3.pack()
pass_entry.pack()
btn.pack()
textbox.pack()

root.mainloop()
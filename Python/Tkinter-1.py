# 1. Import Tkinter Module
# 2. Create the GUI application main Window
# 3. Add widgets

from tkinter import *# use 'from tkinter import *' to import all classes and functions from the Tkinter module

window = Tk()# tk(0) creates the main application window
window.title('Tkinter Sample Window')
window.geometry('300x300')# Set the dimensions of the window width x height

# Label
greeting = Label(text="Hello User", fg='black', bg='white')# fg is for text color, bg is for background color
# Button 
button = Button(text="Click me", bg='black', fg='white')
# Entry 
entry = Entry(fg="yellow", bg="blue", width=50)


greeting.pack()# pack() method is used to add the widget to the window
button.pack()
entry.pack()

frame = Frame(master=window, relief=RAISED, borderwidth=5)# Create a frame widget used as a container
frame.pack()# relief specifies the type of the border sunset, borderwidth specifies the width of the border
label = Label(master=frame, text='Sample Frame')
label.pack()

textbox = Text(fg='green', bg='yellow')
textbox.pack()
window.mainloop()
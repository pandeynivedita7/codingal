from tkinter import *

# 1. Create the main window
window = Tk()
window.title('Tkinter Sample Window')
window.geometry('300x300')

# 2. Label
greeting = Label(window, text="Hello User", fg='black', bg='white')
greeting.pack()

# 3. Button with functionality
def on_click():
    greeting.config(text="Button Clicked!")

button = Button(window, text="Click me", bg='black', fg='white', command=on_click)
button.pack()

# 4. Entry
entry = Entry(window, fg="yellow", bg="blue", width=50)
entry.pack()

# 5. Frame
frame = Frame(master=window, relief=RAISED, borderwidth=5)
frame.pack()

label = Label(master=frame, text='Sample Frame')
label.pack()

# 6. Textbox
greeting = Text(window, fg='green', bg='yellow', height=5, width=30)
greeting.pack()

# 7. Keep the window running
window.mainloop()

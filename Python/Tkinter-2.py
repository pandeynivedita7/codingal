import tkinter as tk

window = tk.Tk()

for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,# use relief to specify the type of border
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)#Grid layout manager to position the frames in a grid x and y
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack()#pack() method is used to add the widget to the frame

window.mainloop()# Start the GUI event loop



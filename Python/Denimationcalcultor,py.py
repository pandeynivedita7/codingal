from tkinter import *
from tkinter import messagebox

class DenominationCalculator:
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x400")
        self.root.title("Denomination Calculator")
        self.root.config(bg="#f0f0f0")
        
        # Title Label
        title_label = Label(root, text="Denomination Calculator", 
                           font=("Arial", 18, "bold"), bg="#f0f0f0")
        title_label.pack(pady=20)
        
        # Input Frame
        input_frame = Frame(root, bg="#f0f0f0")
        input_frame.pack(pady=10)
        
        Label(input_frame, text="Enter Amount:", font=("Arial", 12), bg="#f0f0f0").pack(side=LEFT, padx=10)
        
        self.amount_entry = Entry(input_frame, font=("Arial", 12), width=20)
        self.amount_entry.pack(side=LEFT, padx=5)
        
        # Calculate Button
        calc_button = Button(root, text="Calculate", font=("Arial", 12, "bold"), 
                            bg="#4CAF50", fg="white", command=self.calculate, padx=20, pady=10)# padx and pady location
        calc_button.pack(pady=15)
        
        # Result Frame
        result_frame = Frame(root, bg="white", relief=SUNKEN, bd=2)
        result_frame.pack(pady=15, padx=20, fill=BOTH, expand=True)
        
        Label(result_frame, text="Results:", font=("Arial", 12, "bold"), 
              bg="white", justify=LEFT).pack(anchor=NW, padx=10, pady=10)#n,s,w,e
        
        # Result Display
        self.result_text = Text(result_frame, font=("Arial", 11), height=10, width=50)
        self.result_text.pack(padx=10, pady=10, fill=BOTH, expand=True)
        self.result_text.config(state=DISABLED)
        
        # Reset Button
        reset_button = Button(root, text="Reset", font=("Arial", 12, "bold"), 
                             bg="#f44336", fg="white", command=self.reset, padx=20, pady=10)
        reset_button.pack(pady=10)
    
    def calculate(self):
        try:
            amount = int(self.amount_entry.get())
            
            if amount <= 0:
                messagebox.showerror("Error", "Please enter a positive amount!")
                return
            
            # Calculate denominations
            notes_2000 = amount // 2000
            remaining = amount % 2000
            #** power function 2 raise floor division // whole % reminder
            notes_500 = remaining // 500
            remaining = remaining % 500
            # notes_500 = remaining // 50
            # remaining = remaining % 50
            notes_100 = remaining // 100
            remaining = remaining % 100
            
            # Display results
            self.result_text.config(state=NORMAL)
            self.result_text.delete(1.0, END)
            
            result = f"Amount Entered: Rs. {amount}\n\n"
            result += f"Number of Rs. 2000 notes: {notes_2000}\n"
            result += f"Number of Rs. 500 notes: {notes_500}\n"
            result += f"Number of Rs. 100 notes: {notes_100}\n"
            result += f"\nTotal Notes Used: {notes_2000 + notes_500 + notes_100}\n"
            
            if remaining > 0:
                result += f"\nRemaining Amount: Rs. {remaining}\n"
                result += "(Cannot be denominated with 2000, 500, 100)"
            else:
                result += f"\nTotal Amount Covered: Rs. {amount}"
            
            self.result_text.insert(1.0, result)
            self.result_text.config(state=DISABLED)
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number!")
    
    def reset(self):
        self.amount_entry.delete(0, END)
        self.result_text.config(state=NORMAL)
        self.result_text.delete(1.0, END)
        self.result_text.config(state=DISABLED)
        self.amount_entry.focus()

# Create main window
root = Tk()
app = DenominationCalculator(root)
root.mainloop()
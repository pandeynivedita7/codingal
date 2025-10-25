from tkinter import *

# Function to calculate Simple and Compound Interest
def calculate_interest():
    try:#test block
        principal = float(entry_principal.get())
        rate = float(entry_rate.get())
        time = float(entry_time.get())

        # Simple Interest formula
        simple_interest = (principal * rate * time) / 100

        # Compound Interest formula
        compound_interest = principal * ((1 + rate / 100) ** time) - principal

        # Display results
        label_result_si.config(text=f"Simple Interest: ₹{simple_interest:.2f}")
        label_result_ci.config(text=f"Compound Interest: ₹{compound_interest:.2f}")
    except ValueError:#if error in your try it will come to except
        label_result_si.config(text="Invalid input. Enter numeric values.")
        label_result_ci.config(text="")

# Setup main window
window = Tk()
window.title("Interest Calculator App")
window.geometry("400x300")
window.resizable(False, False)

# Labels and Entry fields
Label(window, text="Principal Amount (₹):").grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_principal = Entry(window)
entry_principal.grid(row=0, column=1, padx=10, pady=10)

Label(window, text="Rate of Interest (% per year):").grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_rate = Entry(window)
entry_rate.grid(row=1, column=1, padx=10, pady=10)

Label(window, text="Time Period (in years):").grid(row=2, column=0, padx=10, pady=10, sticky="w")
entry_time = Entry(window)
entry_time.grid(row=2, column=1, padx=10, pady=10)

# Button to calculate
btn_calculate = Button(window, text="Calculate", command=calculate_interest)
btn_calculate.grid(row=3, column=0, columnspan=2, pady=15)

# Labels to display results
label_result_si = Label(window, text="", fg="blue")
label_result_si.grid(row=4, column=0, columnspan=2)

label_result_ci = Label(window, text="", fg="green")
label_result_ci.grid(row=5, column=0, columnspan=2)

# Start GUI event loop
window.mainloop()

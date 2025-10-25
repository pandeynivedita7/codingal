import tkinter as tk
from tkinter import messagebox

def show_profile():
    name = name_entry.get()
    age = age_entry.get()
    grade = grade_entry.get()
    student_id = id_entry.get()

    if not (name and age and grade and student_id):
        messagebox.showerror("Error", "Please fill out all fields.")
        return

    profile_text = f"""
    ----------------------------
            STUDENT PROFILE
    ----------------------------
    Name       : {name}
    Age        : {age}
    Grade      : {grade}
    Student ID : {student_id}
    ----------------------------
    """
    output_label.config(text=profile_text)

# GUI window setup
window = tk.Tk()
window.title("Student Profile Card")
window.geometry("400x400")
window.config(bg="#f0f0f0")

# Labels and Entry widgets
tk.Label(window, text="Name:", bg="#f0f0f0").pack()
name_entry = tk.Entry(window)
name_entry.pack()

tk.Label(window, text="Age:", bg="#f0f0f0").pack()
age_entry = tk.Entry(window)
age_entry.pack()

tk.Label(window, text="Grade:", bg="#f0f0f0").pack()
grade_entry = tk.Entry(window)
grade_entry.pack()

tk.Label(window, text="Student ID:", bg="#f0f0f0").pack()
id_entry = tk.Entry(window)
id_entry.pack()

# Button to show profile
tk.Button(window, text="Show Profile", command=show_profile, bg="#4caf50", fg="white").pack(pady=10)

# Output label
output_label = tk.Label(window, text="", justify="left", bg="#ffffff", font=("Courier", 10), relief="groove", bd=2)
output_label.pack(padx=10, pady=10, fill="both", expand=True)

window.mainloop()

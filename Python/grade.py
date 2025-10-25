# Input: Marks from user
marks = float(input("Enter your marks (0 to 100): "))

# Grading logic using if-elif-else
if marks < 0 or marks > 100:
    print("Invalid marks! Please enter a value between 0 and 100.")
elif marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 50:
    print("Grade: D")
else:
    print("Grade: F (Fail)")

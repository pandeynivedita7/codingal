marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A+")
else:
    if marks >= 75:
        print("Grade: A")
    else:
        if marks >= 60:
            print("Grade: B")
        else:
            if marks >= 40:
                print("Grade: C")
            else:
                print("Grade: F (Fail)")

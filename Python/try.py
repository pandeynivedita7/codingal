try:
    # Ask the user to enter their age
    age = int(input("Enter your age: "))

    # Check if the entered age is within a valid range
    if age < 0 or age > 150:
        print("Invalid age! Age should be between 0 and 150.")
    else:
        print("Your age is:", age)

        # Check if age is even or odd
        if age % 2 == 0:
            print("Your age is even.")
        else:
            print("Your age is odd.")

except ValueError:
    # Handles non-integer inputs
    print("Invalid input! Please enter a valid integer for age.")

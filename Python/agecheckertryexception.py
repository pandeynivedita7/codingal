def check_age():
    try:
        age = int(input("Enter your age: "))

        # Check for validity
        if age <= 0 or age > 120:
            print("Invalid age entered. Please enter a value between 1 and 120.")
        else:
            print(f"Valid age: {age}")
            
            # Check even or odd
            if age % 2 == 0:
                print("The age is even.")
            else:
                print("The age is odd.")
    
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# Run program
check_age()

import math # library math 
#import library math operation math

# Step 1: Input
number = float(input("Enter a number to find its square root: "))

# Step 2: Validation
if number < 0:
    print("Square root of negative number is not real (use complex numbers if needed).")
else:
    # Step 3: Compute square root
    square_root = math.sqrt(number)
    
    # Step 4: Output
    print(f"The square root of {number} is {square_root}")

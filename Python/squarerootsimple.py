import math#library
number = float(input("Enter a number: "))
square_root = math.sqrt(number)  # Will still compute sqrt for negative input (but not complex)
print("Square root is:", square_root)

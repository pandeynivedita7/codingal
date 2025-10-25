import math  # for using the value of pi

# Function to calculate circumference
def circumference(radius):
    return 2 * math.pi * radius

# Taking input from user
r = float(input("Enter the radius of the circle: "))

# Calling the function and displaying result
print("The circumference of the circle is: ",circumference(r))

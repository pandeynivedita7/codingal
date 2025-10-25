# Define function to calculate cube
def cube(number):
    return number * number * number

# Define a function which executes cube function only if number is divisible by 3
def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False

# Display results
print(by_three(9))  # Should print 729
print(by_three(4))  # Should print False
def factorial(x):
    '''this is a recursive function to find the factorial of an integer'''
    if x == 0 or x == 1:
        return 1
    else:
        # calling function inside the same function
        return x * factorial(x - 1)

# Display docstring
print(factorial.__doc__)

# Display results
print("The factorial of 0:", factorial(0))
print("The factorial of 1:", factorial(1))
print("The factorial of 2:", factorial(2))
print("The factorial of 4:", factorial(4))
print("The factorial of 5:", factorial(5))
print("The factorial of 10:", factorial(10))

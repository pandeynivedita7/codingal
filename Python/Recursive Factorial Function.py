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

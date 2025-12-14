def factorial(x):
    '''this is a recursive function to find the factorial of an integer '''#__doc__ explaination 
    # is a part code that is not executed
    if x == 0 or x == 1:
        return 1# 5! = 5*4*3*2*1
    else:
        # calling function inside a function
        return x * factorial(x - 1)#recursion

# display result
print(factorial.__doc__)
print("The factorial of 0:", factorial(0))
print("The factorial of 1:", factorial(1))
print("The factorial of 4:", factorial(4))#4*3*2*1
print("The factorial of 5:", factorial(5))
print("The factorial of 10:", factorial(10))

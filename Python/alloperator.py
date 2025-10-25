# Python program to demonstrate logical operators: and, or, not

# Define some variables
a = True
b = False

print("Logical Operators in Python")
print("----------------------------")

# AND Operator
print("a and b =", a and b)  # False, because one operand is False
print("True and True =", True and True)  # True
print("False and False =", False and False)  # False

# OR Operator
print("a or b =", a or b)  # True, because one operand is True
print("True or True =", True or True)  # True
print("False or False =", False or False)  # False

# NOT Operator
print("not a =", not a)  # False, because a is True
print("not b =", not b)  # True, because b is False

# Combined Expressions
x = 10
y = 20
z = 10

print("\nCombined Expressions:")
print("x == z and y > x:", x == z and y > x)  # True and True => True
print("x == y or y < x:", x == y or y < x)  # False or False => False
print("not(x != z):", not(x != z))  # not False => True

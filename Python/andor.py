# Python program to demonstrate 'and' and 'or' operators

# Define values
a = 5
b = 10
c = 5

print("Demonstrating 'and' and 'or' operators\n")

# Using 'and' operator
print("Using 'and' operator:")
print("(a == c) and (b > a):", (a == c) and (b > a))  # True and True=>True
print("(a == b) and (b > a):", (a == b) and (b > a))  # false and true=>false
print("(a == c) and (b < a):", (a == c) and (b < a))  # true and false=>false

# Using 'or' operator
print("\nUsing 'or' operator:")
print("(a == c) or (b < a):", (a == c) or (b < a))  # true or false=>true
print("(a == b) or (b < a):", (a == b) or (b < a))  # false or false=>false
print("(a == b) or (b > a):", (a == b) or (b > a))  # False or true=>true
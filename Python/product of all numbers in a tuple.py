# Program to calculate product of all numbers in a tuple

# Given tuple
numbers = (2, 3, 4, 5)

product = 1  # start with 1 (multiplicative identity)

for num in numbers:
    product *= num   # multiply each element product=product*num

print("Tuple:", numbers)
print("Product of all numbers:", product)

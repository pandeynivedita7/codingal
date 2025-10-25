# Program to calculate the product of numbers in a tuple

def tuple_product(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

# Example tuple
my_tuple = (2, 3, 4, 5)

# Calculate product
result = tuple_product(my_tuple)

print("Tuple:", my_tuple)
print("Product of tuple elements:", result)

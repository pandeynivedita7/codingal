# Empty tuple
my_tuple = ()
print(my_tuple)

# Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)

# Tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

# Nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)

# Accessing tuple elements using indexing
my_tuple = ('p', 'e', 'r', 'm', 'i', 't')
print(my_tuple[0])  # first element
print(my_tuple[5])  # last element

# Nested tuple
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

# Nested index
print(n_tuple[0][3])  # accessing 's' from "mouse"
print(n_tuple[1][1])  # accessing 4 from [8, 4, 6]

# Slicing
print("Sliced:", my_tuple[1:4])  # slice from index 1 to 3

# Iterating through tuple
for letter in my_tuple:
    print("Hello", letter)

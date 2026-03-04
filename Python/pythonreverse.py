# Python code to reverse a string

# Method 1: Using slicing
string = "Hello World"
reversed_string = string[::-1]
print(f"Original: {string}")
print(f"Reversed: {reversed_string}")

# Method 2: Using a loop
def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

result = reverse_string("Python")
print(f"Reversed: {result}")

# Method 3: Using reversed() function
string = "Reverse me"
reversed_string = "".join(reversed(string))
print(f"Reversed: {reversed_string}")

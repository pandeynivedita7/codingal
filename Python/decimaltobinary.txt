# Function to convert decimal to binary
def decimal_to_binary(decimal_num):
    binary = ""
    if decimal_num == 0:
        return "0"
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary = str(remainder) + binary
        decimal_num = decimal_num // 2
    return binary

# Taking input from user
decimal_input = int(input("Enter a decimal number: "))

# Converting and printing binary
binary_output = decimal_to_binary(decimal_input)
print("Binary equivalent:", binary_output)

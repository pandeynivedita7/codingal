def sum_of_numbers(numbers):
    total = 0
    for num in numbers:# for var in range:
        total = total+ num
    return total

# Example usage
my_list = [10, 20, 30, 40, 50]
print("Sum of numbers:", sum_of_numbers(my_list))

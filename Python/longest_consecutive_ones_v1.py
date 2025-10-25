def longest_consecutive_ones_v1(n):
    binary = bin(n)[2:]  # Convert to binary, remove '0b' prefix
    max_count = 0
    current_count = 0

    for bit in binary:
        if bit == '1':
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0

    return max_count

# Test
num = int(input("Enter a number: "))
print(f"Binary representation: {bin(num)[2:]}")
print(f"Longest consecutive 1's: {longest_consecutive_ones_v1(num)}")
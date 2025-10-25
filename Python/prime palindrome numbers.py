a = 3000

for num in range(1, a + 1):
    c = 0
    rev = 0
    temp = num

    # Check if number is prime
    for i in range(1, temp + 1):
        if temp % i == 0:
            c += 1

    # Prime numbers have exactly two divisors
    if c == 2:
        temp = num
        rev = 0

        # Reverse the number
        while temp > 0:
            rev = rev * 10 + (temp % 10)
            temp //= 10

        # Check if number is palindrome
        if rev == num:
            print(num)

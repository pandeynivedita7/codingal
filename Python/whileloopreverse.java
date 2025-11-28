num = 12345        # number to reverse
rev = 0            # variable to store reversed number

while num != 0:
    digit = num % 10          # extract last digit
    rev = rev * 10 + digit    # add digit to reversed number
    num = num // 10           # remove last digit

print("Reversed number:", rev)

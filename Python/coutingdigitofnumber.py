# Input from user
num = int(input("Enter a number: "))#5

# Make sure number is positive for counting digits
n = abs(num)

# If number is 0, it has 1 digit
if n == 0:
    count = 1
else:
    count = 0
    while n > 0:#5>0
        n = n // 10  # Remove last digit  answer 0
        count += 1   # Increase digit count 1

print("Total digits in the number:", count)

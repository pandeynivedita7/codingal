num = int(input("Enter a number: "))#153
count = 0
while num > 0:#true
    num = num // 10    # Remove last digit
    count += 1 
print("Total digits in the number:", count)
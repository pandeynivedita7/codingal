num = int(input("Enter a number: "))
temp = num
count = 0
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10#temp=temp//10
    count += 1#count=count+1
print("Total digits:", count)
print("Reversed number:", reverse)

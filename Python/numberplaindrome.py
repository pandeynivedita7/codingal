#Take input from user
num = int(input("Enter a number: "))
rev = 0
#checking each digit are the same backward and forward
temp = num
while temp>0:
    rem = temp%10
    rev = rem + (rev*10)
    temp = int(temp/10)
#display the result
if rev==num:
    print("\nIt is a Palindrome Number")
else:
    print("\nIt is not a Palindrome Number")
# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:# while condition that number should be greater than 0
   digit = temp % 10 #reminder individual number
   sum += digit **3 # **raise to 2^2 2**2 sum=sum+digit**3
   temp //= 10 #// floor division no decimal vaule temp=temp//10 
   #by this 3 step you will get armstrong number

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
 # 153 = 1^3 + 5^3 + 3^3 =153 armstraong
 # separata


   # 153=1^3+5^3+3^3=1+125+9=153 An Armstrong number (also called a narcissistic number) is a number that is equal to the sum of its own digits each raised to the power of the number of digits.
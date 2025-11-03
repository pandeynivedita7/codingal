#take two input from user
lower = int(input("Enter a lower range: "))#1
upper = int(input("Enter a upper range: "))#10

print("Prime numbers between", lower, "and", upper, "are:")
#iterate loop from lower limit to upper limit
for num in range(lower, upper + 1):#1 to 10
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
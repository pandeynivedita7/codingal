#take two input from user
lower = int(input("Enter a lower range: "))#start
upper = int(input("Enter a upper range: "))#end

print("Prime numbers between", lower, "and", upper, "are:")
#iterate loop from lower limit to upper limit
for num in range(lower, upper + 1):#to transeval
   # all prime numbers are greater than 1
   if num > 1:#enter number greater then 1
       for i in range(2, num):# for i in range(start,end)
           if (num % i) == 0:#even
               break
       else:
           print(num)
           #nested loop having mulitple loop
def flips(num1,num2):
  flip = 0
  while (num1 > 0 or num2 > 0):# while condition stmt
   t1 = num1 & 1# or its true if either condition is true
   t2 = num2 & 1
   if t1 != t2:# not! equat not 
    flip += 1# flip=flip +1
   num1 >>= 1
   num2 >>= 1
  return flip
num1 = int(input("Enter first number: "))#10 1010
num2 = int(input("Enter second number: "))#7 0111
print("Number of flips needed: ", flips(num1, num2))
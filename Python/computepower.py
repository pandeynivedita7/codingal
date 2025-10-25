def computePower(x, y):  
  result = 1
  while y>0:#Loops while y is greater than 0. The loop continues until we've processed all bits of y.
      if(y%2==0): #Checks if y is even. y%2==0 means y is divisible by 2 (no remainder). even number
          x=x*x#If y is even, square x. This is based on the property: x^(2n) = (x^2)^n
          y>>=1
      else:#false odd number
          result = result * x#If y is odd, multiply the current x value to the result.
          y = y - 1#Subtract 1 from y to make it even, so the next iteration can divide it.
   return result
x = int(input("Enter x for x^y : "))
y = int(input("Enter y for x^y : "))
print("Total : ",(computePower(x, y)))



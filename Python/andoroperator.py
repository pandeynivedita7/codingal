# Example 5: Using 'and' for boolean truth check
a = 10# true
b = 12#true
c = 0#false
# boolean 0 Aand 1
if a and b and c:# all should be true to get true a=t b=t c=f
    print("All the numbers have boolean value as True")
else:# false
    print("At least one number has boolean value as False")

# Example 6: Using 'or' to check if any number is greater than 0
a = 10
b = -10
c = 0

if a > 0 or b > 0:# a>0 true or b>-10 false 
    print("Either of the numbers is greater than 0")#this answer
else:
    print("No number is greater than 0")

if b > 0 or c > 0:#B>0 false c>0 false
    print("Either of the numbers is greater than 0")
else:
    print("No number is greater than 0")#false

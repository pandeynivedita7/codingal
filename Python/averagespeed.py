a = int(input("Enter value 1: "))# i an thing a b and c is a car
b = int(input("Enter value 2: "))# so 
c = int(input("Enter value 3: "))

avg = (a + b + c) / 3
print("avg =", avg)

if avg > a and avg > b and avg > c:# and means all true
    print("%d is higher than %d, %d, %d /n" % (avg, a, b, c))
elif avg > a and avg > b:# but for check using and operator means all true
    print("%d is higher than %d, %d" % (avg, a, b))
elif avg > a and avg > c:
    print("%d is higher than %d, %d" % (avg, a, c))
elif avg > b and avg > c:
    print("%d is higher than %d, %d" % (avg, b, c))
elif avg > a:
    print("%d is just higher than %d" % (avg, a))
elif avg > b:
    print("%d is just higher than %d" % (avg, b))
elif avg > c:#%
    print("%d is just higher than %d" % (avg, c))
else:
    print("invalid input")
    #print(""%.2f" % avg)  # to print decimal value till 2 places
# a=14
#print("the value of a is" % a) old styled
#%d int % .2f decimal value till 2 decimal float %s string
#print("the value of a is %d" % a) new styled
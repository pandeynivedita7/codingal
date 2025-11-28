# Python program to illustrate the use of 'is' identity operator
# what is the use of type() check the variable is int float or string
x = 5
if type(x) is int:#true
    print("true")
else:
    print("false")

x = 5.0
if type(x) is not float:#False
    print("true")
else:
    print("false")

x = 20
y = 20
if x is y:#Flase because different container
    print("x & y have SAME identity")

y = 30
if x is not y:#True
    print("x & y have DIFFERENT identity")

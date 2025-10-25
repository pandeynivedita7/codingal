x = [1, 2, 3]
y = x# same memory location
z = [1, 2, 3]# but different container location different memeory object

print(x is y)      # True — because y refers to the same object as x
print(x is z)      # False — because z is a different object with same content
print(x == z)      # True — because content of x and z are the same
#== is use to check value x=5 assignment x==y check comparsion
print(x is not z)  # True — because x and z are not the same object

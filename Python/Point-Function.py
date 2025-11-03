# Create class
class Point:
    def __init__(self, x=0, y=0):#default of x and y 0,0
        self.x = x
        self.y = y

	# Method to print points in coordinate format
    def __str__(self):#special function
        return "({0}, {1})".format(self.x, self.y)#return(x,y)

# Create Object
p1 = Point(2, 3)
p2=Point()
print(p1)#2,3
print(p2)#0,0

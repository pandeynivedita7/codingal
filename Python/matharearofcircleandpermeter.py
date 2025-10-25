import math   # to use the value of pi

class Circle:
    # constructor to initialize radius
    def __init__(self, radius):
        self.radius = radius

    # method to compute area
    def area(self):
        return math.pi * (self.radius ** 2)

    # method to compute perimeter (circumference)
    def perimeter(self):
        return 2 * math.pi * self.radius


# ----- Object Creation -----
# user input
r = float(input("Enter the radius of the circle: "))

c = Circle(r)   # create object with given radius

# call methods
print("Area of circle:", c.area())
print("Perimeter of circle:", c.perimeter())

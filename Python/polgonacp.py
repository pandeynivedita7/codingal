class Polygon:
    def area(self):
        pass

class Rectangle(Polygon):
    def __init__(self, l, w):
        self.l = l
        self.w = w
    def area(self):
        return self.l * self.w

class Triangle(Polygon):
    def __init__(self, b, h):
        self.b = b
        self.h = h
    def area(self):
        return 0.5 * self.b * self.h

# Driver code
r = Rectangle(5, 4)
t = Triangle(6, 3)

print("Rectangle area:", r.area())
print("Triangle area:", t.area())

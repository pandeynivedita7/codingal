import turtle

my_wn = turtle.Screen()
my_wn.bgcolor("light blue")
my_wn.title("Spiral Circle")

my_pen = turtle.Turtle()
my_pen.speed(0)  # Fastest speed 0 fastest 0 fast

size = 1  # Initial radius

while size < 200:  # Limit the spiral condition
    my_pen.circle(size)
    my_pen.left(20)  # Change angle for spiral effect
    size += 2  # Increase radius each time size=size+2

my_wn.mainloop()  # Keeps the window open

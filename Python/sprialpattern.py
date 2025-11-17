import turtle  # importing library

my_wn = turtle.Screen()
my_wn.bgcolor("light blue")  # screen background color
my_wn.title("sprial")

my_pen = turtle.Turtle()
size =0

while True:  # infinite loop
    for i in range(4):  # draws a square
        my_pen.fd(size + 1)# unit forward+position
        my_pen.left(90)
        size = size - 5# size=0-5 size=-5+5
    size = size + 1

import turtle

# Create screen and set background color
screen1 = turtle.Screen()
screen1.bgcolor("lightblue")
screen1.setup(300, 400)# width and height
screen1.title("Triangle")

# Create turtle object
board = turtle.Turtle()

# Draw a triangle
for i in range(3):
    board.forward(100)
    board.left(120)

turtle.done()

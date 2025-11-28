import turtle# drawing or create a canvas

# creating canvas
turtle.Screen().bgcolor("Orange")

sc = turtle.Screen()
sc.setup(400, 300)# window size width and height

turtle.title("Welcome to Turtle Window")

# turtle object creation
board = turtle.Turtle()# canvas

# creating a square
for i in range(4):
	board.forward(100)# forward and backward movement
	board.left(90)#  left and right it will angle
	i = i+1


turtle.done()
# # hold the window


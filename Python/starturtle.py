import turtle

turtle.Screen().bgcolor("Red")
board = turtle.Turtle()# default value 200*200
 
# first triangle for star
board.forward(100) # draw base
 
board.left(120)#things you are writing in bracket are steps
board.forward(100)
 
board.left(120)
board.forward(100)
 
board.penup()
board.right(150)
board.forward(50)
 
# second triangle for star
board.pendown()
board.right(90)
board.forward(100)
 
board.right(120)
board.forward(100)
 
board.right(120)
board.forward(100)
 
turtle.done()## hold the window
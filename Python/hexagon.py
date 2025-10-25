import turtle  # importing library

turtle.Screen().bgcolor("orange")#. dot function turtle method bg backgroud colour 
turtle.Screen().setup(300, 400)# width and height window size 

polygon = turtle.Turtle()  # defined variable

num_sides = 8  # variable

side_length = 70
angle = 360.0 / num_sides

# iterate loop for total number of sides
for i in range(num_sides):
    polygon.backward(side_length)
    polygon.left(angle)

turtle.done()

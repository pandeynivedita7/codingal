import turtle    #importing library
turtle.Screen().bgcolor("orange")#setting background color
turtle.Screen().setup(300,400)# size of window
polygon = turtle.Turtle() #defined variable
 
num_sides = 6 #variable
side_length = 70#variable like length of side unit
angle = 360.0 / num_sides# calculating angle of polygon
#iterate loop for total number of side
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
     
turtle.done()# pause the screen to show output


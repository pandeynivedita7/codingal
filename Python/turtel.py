import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Race Game")
screen.bgcolor("lightblue")

# Function to draw the race track
def draw_track():
    line = turtle.Turtle()
    line.penup()
    line.goto(-160, -100)
    line.speed(0)
    for step in range(16):
        line.write(step, align='center')
        line.right(90)
        line.forward(200)
        line.backward(200)
        line.left(90)
        line.forward(20)
    line.hideturtle()

# Function to create a turtle with color and starting y-position
def create_turtle(color, y_pos):
    racer = turtle.Turtle()
    racer.shape("turtle")
    racer.color(color)
    racer.penup()
    racer.goto(-160, y_pos)
    racer.pendown()
    return racer

# Function to start the race
def race(t1, t2):
    while t1.xcor() < 140 and t2.xcor() < 140:
        t1.forward(random.randint(1, 5))
        t2.forward(random.randint(1, 5))
    
    # Determine the winner
    if t1.xcor() >= 140 and t2.xcor() >= 140:
        print("It's a tie!")
    elif t1.xcor() >= 140:
        print("Red turtle wins!")
    else:
        print("Blue turtle wins!")

# Main function to run the game
def main():
    draw_track()
    
    red = create_turtle("red", -40)
    blue = create_turtle("blue", 40)

    race(red, blue)
    
    # Keep the window open until user closes it
    turtle.done()

# Run the main function
main()

import turtle
import random

def setup_race():
    screen = turtle.Screen()
    screen.title("Turtle Race Game")
    screen.bgcolor("lightblue")
    
    # Draw the finish line
    finish_line = turtle.Turtle()
    finish_line.penup()
    finish_line.goto(200, -100)
    finish_line.pendown()
    finish_line.left(90)
    finish_line.forward(200)
    finish_line.hideturtle()
    
    return screen

def create_turtle(color, x, y):
    t = turtle.Turtle()
    t.shape("turtle")
    t.color(color)
    t.penup()
    t.goto(x, y)
    return t

def race(turtles):
    winner = None
    while winner is None:
        for t in turtles:
            t.forward(random.randint(1, 10))
            if t.xcor() >= 200:
                winner = t.color()[0]
                break
    return winner

def main():
    screen = setup_race()
    
    # Creating turtles
    colors = ["red", "blue", "green", "yellow"]
    turtles = []
    start_y = -50
    for color in colors:
        turtles.append(create_turtle(color, -200, start_y))
        start_y += 30
    
    # Start the race
    winner = race(turtles)
    print(f"The winner is {winner} turtle!")
    
    screen.mainloop()

if __name__ == "__main__":
    main()

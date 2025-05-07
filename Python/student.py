import turtle

def draw_profile_card(name, age, grade, color, hobby):
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.penup()
    t.goto(-150, 100)
    t.pendown()

    # Validate color input
    try:
        t.fillcolor(color)
    except turtle.TurtleGraphicsError:
        print(f"Invalid color '{color}' entered. Using default color 'lightblue'.")
        t.fillcolor("lightblue")

    t.begin_fill()
    for _ in range(2):
        t.forward(300)
        t.right(90)
        t.forward(200)
        t.right(90)
    t.end_fill()

    t.penup()
    t.goto(-130, 60)
    t.color("black")
    try:
        t.write(f"Name: {name}", font=("Arial", 14, "normal"))
        t.goto(-130, 30)
        t.write(f"Age: {age}", font=("Arial", 14, "normal"))
        t.goto(-130, 0)
        t.write(f"Grade: {grade}", font=("Arial", 14, "normal"))
        t.goto(-130, -30)
        t.write(f"Favorite Color: {color}", font=("Arial", 14, "normal"))
        t.goto(-130, -60)
        t.write(f"Hobby: {hobby}", font=("Arial", 14, "normal"))
    except turtle.TurtleGraphicsError:
        print("An error occurred while writing text. Check if the font is supported.")

# Sample data input
name = input("Enter your name: ")
age = input("Enter your age: ")
grade = input("Enter your grade: ")
color = input("Enter your favorite color: ")
hobby = input("Enter your hobby: ")

draw_profile_card(name, age, grade, color, hobby)

turtle.done()

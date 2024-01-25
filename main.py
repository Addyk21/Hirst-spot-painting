import turtle
import random
import extract_color

turtle.colormode(255)
# getting a list of color codes
color_list = extract_color.get_palette()
# creating an object of Turtle class
brush = turtle.Turtle()
# creating a variable to move the turtle towards the bottom of screen
y_cord = -300
brush.speed("fastest")
brush.penup()
brush.hideturtle()
brush.goto(-300, -300)
for _ in range(8):
    for _ in range(10):
        brush.dot(35, random.choice(color_list))
        brush.fd(70)
    y_cord += 70
    brush.goto(-300, y_cord)  # moves the turtle above the last starting row

screen = turtle.Screen()
screen.exitonclick()

#!/usr/bin/python3

# Draw on the command line using turtle module

import turtle

scr = turtle.Screen()
scr.bgcolor("black")
turtle.shape("turtle")
#turtle.hideturtle()

for i in range(0,10):
    turtle.begin_fill()
    # Move right 36 degrees
    turtle.right(36)
    if (i % 2) == 0:
        color = "green"
        turtle.pensize(3)
        turtle.penup()
    else:
        color = "red"
        turtle.pendown()

    turtle.color(color)
    turtle.fillcolor(color)

    for x in range(0,5):
        # Move forward 100px
        turtle.forward(100)
        turtle.right(72)
    turtle.end_fill()
turtle.exitonclick()

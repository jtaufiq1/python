#!/usr/bin/python3

# Use turtle to draw circle

import turtle

triangle = turtle.Turtle()
triangle.hideturtle()
triangle.pensize(3)

for i in range(0,5):
    triangle.forward(100)
    triangle.right(144)

turtle.exitonclick()

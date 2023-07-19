#!/usr/bin/python3

import turtle
# Draw a square

sqr = turtle.Turtle()
sqr.pensize(3)
sqr.hideturtle()

sqr.color("red","green")
sqr.begin_fill()
for i in range(0,4):
    sqr.right(90)
    sqr.forward(100)
sqr.end_fill()

turtle.exitonclick()

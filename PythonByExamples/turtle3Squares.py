#!/usr/bin/python3

import turtle
import random

# Draw 3 squares in a row with different fill color each
sqr = turtle.Turtle()
sqr.pensize(3)
#sqr.shape("arrow")
sqr.hideturtle()
COLORS = ("red","blue","green","pink","orange","cyan","grey","brown")

for i in range(1,4):
    fillColor = random.choice(COLORS)
    sqr.color("black",fillColor)

    sqr.begin_fill()
    sqr.pendown()
    for s in range(0,4):
        sqr.right(90)
        sqr.forward(80)
    sqr.penup()
    sqr.end_fill()
    if i != 3:
        sqr.forward(100)
turtle.exitonclick()

#!/usr/bin/python3

# Draw a pentagon with 6 random fill colors

import turtle
import random
#scr = turtle.Screen()
#scr.bgcolor("black")
turtle.hideturtle()
#turtle.shape("turtle")

COLORS = ("red","blue","green","pink","orange","cyan","grey","brown")
for i in range(0,10):
    fillColor = random.choice(COLORS)
    turtle.color(fillColor)

    turtle.right(36)        # Turn 36 degree clockwise

    turtle.begin_fill()
    for x in range(0,5):
        turtle.forward(85) # Move forward 100px
        turtle.right(72)
    turtle.end_fill()
turtle.exitonclick()


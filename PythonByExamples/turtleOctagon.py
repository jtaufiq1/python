#!/usr/bin/python3

# Draw on the command line using turtle module

import turtle
turtle.hideturtle()
#turtle.shape("turtle")

for i in range(0,12):
    turtle.right(36)        # Turn 36 degree clockwise

    for x in range(0,8):
        turtle.forward(60) # Move forward 100px
        turtle.right(45)
turtle.exitonclick()


#!/usr/bin/python3

# Use turtle to draw circle

import turtle

turtle.shape("arrow")
turtle.hideturtle()

for i in range(0,361):
    turtle.forward(1)
    turtle.right(1)
turtle.exitonclick()

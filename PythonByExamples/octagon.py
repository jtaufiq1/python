#!/usr/bin/python3

import turtle
import random

turtle.pensize(3)
colors = ("red","blue","yellow","green","pink","orange")
for i in range(0,8):
    turtle.color(random.choice(colors))
    turtle.forward(50)
    turtle.right(45)

turtle.exitonclick()

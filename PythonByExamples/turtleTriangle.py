#!/usr/bin/python3

# Use turtle to draw circle

import turtle

scr = turtle.Screen()
scr.bgcolor("green")

triangle = turtle.Turtle()
#turtle.shape("arrow")
triangle.hideturtle()
triangle.pensize(2)
triangle.color("red","pink")

triangle.begin_fill()
for i in range(3):
    triangle.forward(-200)
    triangle.left(-120)
triangle.end_fill()

turtle.exitonclick()

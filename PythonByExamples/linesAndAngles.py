#!/usr/bin/python3

# Turtle lines and angles

import turtle

def debug(text, color):
    print(f"[DEBUG]: {text} {color}")

def config(t, ps, ts="arrow", ht=False):
    #scr = turtle.Screen()
    #scr.bgcolor("green")

    t = turtle.Turtle()
    t.shape(ts)
    t.pensize(int(ps))
    if ht == True:
        t.hideturtle()

    return t
#====================== Turtle Configuration ======================
#turtle.shape("arrow")   # Shape
#turtle.hideturtle()     # Hide turtle shape
#turtle.pensize(2)       # Pen size (Line thickness)
arrow = config("arrow", 3, ht=True)
print(f"{arrow}")
#==================================================================

#TODO: Change to use loop

# Line 1
arrow.color("green")   # Line and/or fill color
arrow.right(90)        # Angle
arrow.forward(100)     # Line
debug("Line 1", arrow.color())

#1. Turn Back 180 degrees
debug("penup() and right(180) Back", arrow.color())
arrow.penup()
arrow.right(180)
arrow.forward(100)

# Line 2
arrow.pendown()
arrow.color("red")
arrow.forward(100)
debug("Line 2", arrow.color())

#2. Turn Back 180 degrees
debug("penup() and right(180) Back", arrow.color())
arrow.right(180)
arrow.forward(100)

# Line 3
arrow.pendown()
arrow.color("yellow")
arrow.right(90)
arrow.forward(100)
debug("Line 3", arrow.color())

#3. Turn Back 180 degrees
debug("penup() and right(180) Back", arrow.color())
arrow.penup()
arrow.right(180)
arrow.forward(100)

# Line 4
arrow.pendown()
arrow.color("black")
arrow.forward(100)
debug("Line 4", arrow.color())

turtle.exitonclick()    # Exit

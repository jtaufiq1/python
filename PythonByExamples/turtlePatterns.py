#!/usr/bin/python3

# Draw pattern that changes on each run
# Randomly choose number of lines
#+ Length of each line
#+ and the angle of each turn.

import turtle
import random

random_angle = random.randint(0,360)
random_lines = random.randint(3,11)
random_length = random.randint(20, 100)

for i in range(0, random_lines):
#    for x in range(0,random_lines):
    turtle.right(random_angle)
    turtle.forward(random_length)

turtle.exitonclick()

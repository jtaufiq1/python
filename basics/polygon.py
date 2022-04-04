#!/usr/local/bin/python3
#
# Object Oriented Programming
#+ with Python 3
import turtle

# Begin Class Def
class Polygon:
    def __init__(self, sides, name):
        self.sides = sides
        self.name = name
    def draw(self):
        for i in range(self.sides):
            turtle.forward(100)
            turtle.right(90)
        turtle.done()
# End Class Def


## __main__
square = Polygon(4, "Square")
pentagon = Polygon(5, "Pentagon")

square.draw()

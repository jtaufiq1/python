#!/usr/bin/python3

import math

# Display menu items:
#  1) Square
#  2) Triangle
#  3) Circle
#
#  Enter a number:
#
# Get input to select menu item
# If user selects 1:
#  Get one of the length of square
#  Display the area
# If the user selects 2:
#  Get the base and height of the triangle
#  Display the area: (base * height)/2
# If the user selects 3:
#  Get the radius and depth of circle
#  Display the area and volume
# Else Display an error message

print("Options:")
print(" 1) Square")
print(" 2) Triangle")
print(" 3) Circle")
print()
opt = input("Enter a number: ")

if opt == "1":
    print("Area of Square")
    length = float(input("Length: "))
    area = length ** 2

    print("Area: ", area)
elif opt == "2":
    print("Area of Triangle")
    base = float(input("Base: "))
    height = float(input("Height: "))
    area = (base * height)/2

    print("Area: ", area)
elif opt == "3":
    # Radius & Depth: Area & Volume
    print("Area & Volume of Circle")
    radius = float(input("Radius: "))
    depth = float(input("Depth/Height: "))

    PI = math.pi
    area = PI * (radius **2)
    volume = area * depth

    print("Area: ", round(area, 3))
    print("Volume: ", round(volume, 3))
else:
    print("Error: invalid selection")

print()

#!/usr/bin/python3

import math

# Volume of Circle
# Get radius and depth from input
# Calculate volume: volume = area of circle * depth
#  Area of Circle = PI * (radius**2)
# Display result in 3 decimal places.

print("Enter properties of circle".upper())
radius = float(input("radius: "))
depth = float(input("depth: "))

PI = math.pi
areaOfCircle = round((PI * (radius**2)), 3)
volumeOfCircle = round((areaOfCircle * depth), 3)

print()
print("properties of circle".title())
print("radius: ".title(), radius)
print("depth/height: ".title(), depth)
print("Area: ", areaOfCircle)
print("Volume: ", volumeOfCircle)
print()

#!/usr/bin/python3

(x, y) = (5, 0)
z = 0

try:
    z = x/y
except ZeroDivisionError as e:
    print(f"An error occured: {e}")
except:
    print("something went wrong")

#print(z)

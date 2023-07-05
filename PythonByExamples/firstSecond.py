#!/usr/bin/python3

# Get two numbers
# If first number is greater than second number
#   Output second number and then first number
# Else
#   Output first number and second number

num1 = int(input("First Number: "))
num2 = int(input("Second Number: "))

if num1 >= num2:
    print(num2, num1)
else:
    print(num1, num2)

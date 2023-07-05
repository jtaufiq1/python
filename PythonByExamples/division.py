#!/usr/bin/python3

# Get 2 integers
# Divide second number by the first number
# Display the answer and remainder

print("enter two integers:")
num1 = int(input("First Integer: "))
num2 = int(input("Second Integer: "))

div = num1 // num2
rem = num1 % num2

print(num1, "divided by", num2, "is", str(div)+ ", remainder", rem)

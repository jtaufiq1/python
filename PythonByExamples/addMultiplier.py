#!/usr/bin/python3

# Get three numbers
# Add the first two
# Multiply the results with the third number
# Display the total calculation

print("Add & Multipy")
print()

print("Enter:")
num1 = float(input(" First Number: "))
num2 = float(input(" Second Number: "))
num3 = float(input(" Third Number: "))

sumOfTwo = num1 + num2
total = sumOfTwo * num3

print()
print("The answer is", round(total))

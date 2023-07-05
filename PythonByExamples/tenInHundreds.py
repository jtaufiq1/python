#!/usr/bin/python3

# Number less 10 in number greater than 100
#
# Get number greater than 100
# Get number less than 10
# Divide number greater than 100 by number less than 10
# Output results of division

numberOverHundred: int = int(input("Enter number greater than 100: "))
numberBelowTen: int = int(input("Enter number below 10: "))

results = (numberOverHundred // numberBelowTen)

print(numberBelowTen, "goes into", numberOverHundred, results, "times")

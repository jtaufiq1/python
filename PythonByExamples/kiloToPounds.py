#!/usr/bin/python3

# Convert Kilogram to pounds
# 1Kg = 2204p
#
# Get input Kilogram(s)
# Convert to pounds
# Outputs convertion results

kilogram = float(input("Kilograms(Kg): "))

POUNDS_PER_KG = 2.204
pounds = POUNDS_PER_KG * kilogram

print()
print(kilogram,"KG is equal to", pounds, "pounds")

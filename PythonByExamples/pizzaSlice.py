#!/usr/bin/python3

# Pizza Slice: Total Count
# Number Eaten
# Calculate remainder
# Output remainder in user-friendly format

totalPizzaSlice = input("How many slie of pizza do you have: ")
totalSliceEaten = input("How many slice have you eaten: ")
totalSliceLeft = int(totalPizzaSlice) - int(totalSliceEaten)

print()
print("You ate", totalSliceEaten, "out of the", totalPizzaSlice,\
      "slice of pizza and you have", totalSliceLeft, "slice left.")


#!/usr/bin/python3

# Get total bill after dinning
# Get number of diners
# Divide bill by number of diners
# Output bill for each diner

print("pay bill".upper())
print()

totalBillAfterDinning = input("What is the total Dinning bill? ")
numberOfDiners = input("How many of you went to dine? ")

billForEachDiner: float = float(totalBillAfterDinning) / int(numberOfDiners)

print("Each Diner is paying: $" + str(billForEachDiner))

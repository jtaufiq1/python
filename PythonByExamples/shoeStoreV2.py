#!/usr/bin/python3

# Ask the user for name, age and shoe size of four persons
# Get name of one person in the list
# Display ONLY the name and age

shoe_store = dict()
for i in range(0,4):
    name = input("Enter name: ")
    age = int(input(f"Age of {name}: "))
    shoe_size = int(input(f"Shoe size: "))

    shoe_store[name] = {'age':age,'shoe_size':shoe_size}

print(f"NAME\tAGE")
for p in shoe_store:
    print(f"{p}\t{shoe_store[p]['age']}")

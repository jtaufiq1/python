#!/usr/bin/python3

# Ask the user for name, age and shoe size of four persons
# Get name of one person in the list
# Ask the user to enter a name to remove.

shoe_store = dict()
for i in range(0,4):
    name = input("Enter name: ")
    age = int(input(f"Age of {name}: "))
    shoe_size = int(input(f"Shoe size: "))

    shoe_store[name] = {'age':age,'shoe_size':shoe_size}

remove = input("Enter a name to remove: ")
if remove in shoe_store:
    del shoe_store[remove]
    for p in shoe_store:
        print(f"{p}| {shoe_store[p]['age']} {shoe_store[p]['shoe_size']}")
else:
    print(f"{remove} not in the list")

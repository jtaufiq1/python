#!/usr/bin/python3

# Ask the user for name, age and shoe size of four persons
# Get name of one person in the list
# Display their age and shoe size.

shoe_store = dict()
for i in range(0,4):
    name = input("Enter name: ")
    age = int(input(f"Age of {name}: "))
    shoe_size = int(input(f"Shoe size: "))

    shoe_store[name] = {'age':age,'shoe_size':shoe_size}
    print(f"{name} done")

for x in shoe_store.items():
    print(x)

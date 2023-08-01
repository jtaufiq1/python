#!/usr/bin/python3

# Four Favorite food in dictionary
# Get four favorite food
# Store each in a dictionary.
# Dictionary key starts from 1
# Display the dictionary with key and item
# Get item to remove from the list
# Sort the dictionary
# Display the dictionary

fav_food = dict()
food_list = ['ZT','rice','jollof','stew','yumi']

key = 1
for f in food_list:
    fav_food[key] = f
    key = key + 1
del key

print(f"Type: {type(fav_food)}, ID: {id(fav_food)}")
print(f"Favorite foods: {fav_food}")
#for k,v in fav_food.items():
#    print(f"{v}: {k}")

food = int(input("Remove food: "))
del fav_food[food]

sorted(fav_food)
print(f"Favorite foods: {fav_food.values()}")

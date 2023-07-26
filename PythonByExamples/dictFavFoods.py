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
food_list = ['rice','jollof','stew','yumi']

for i in range(1,5):
    fav_food[i] = food_list[i-1]
print(f"Favorite foods: {fav_food}")

#for k,v in fav_food.items():
#    print(f"{v}: {k}")

food = int(input("Remove food: "))
del fav_food[food]

print(f"Favorite foods: {fav_food.values()}")

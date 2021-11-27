
#!/bin/env python3

# Dictionaries in python
# Dictionary def

person = {
    'id': 26,
    'name': "taufiq gh",
    'age':25,
    'course': "intro to python programming",
    'hobby': "geeky stuffs"
}

car = {
    'brand': "Ford",
    'model': "Mustang",
    'year': 1964
}

ind = {
    'person1':person,
    'vehicle': car
}

# Iterate over dict items
for it in person:
    print(person.get(it))
    
print(person.items())
print(person.values())
print(person.fromkeys('id', 54))

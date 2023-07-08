#!/usr/bin/python3

# Random number generator
import random

num = int(input("How many random numbers do you want? "))
randList = []

for i in range(num):
    rand1 = random.random()
    rand2 = random.random()
    randInt = random.randint(1,100)

    newRand = round((rand1/rand2)*randInt, 1)
    randList.append(newRand)


randList.sort()
if num >= 10:
    print(f"{num} Random Numbers:")
    for r in randList:
        index = randList.index(r)
        if index % 5 == 0:
            sep = '\n'
        else:
            sep = '\t'
            pass
        print(f"{r}", end=sep)
else:
    print(f"\t{num} Random Numbers:{randList}")

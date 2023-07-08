#!/usr/bin/python3

# Random number generator
import random

num = int(input("How many random numbers do you want? "))
randList = []

for i in range(num):
    rand1 = random.random()
    rand2 = random.random()
    randInt = random.randint(1,1000)

    newRand = round((rand1/rand2)*randInt, 1)
    randList.append(newRand)
print(f"\t{num} Random Numbers:{randList}")

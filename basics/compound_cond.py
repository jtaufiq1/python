#!/usr/bin/python3

import sys

# Loops with compound conditionals
# Write to file instead of stdout
with open('test.txt', 'a') as file:
    sys.stdout = file
    for i in range(1,4):
        for j in range(1, 4):
            if (i*j < 5) and (i + j > 3):
                print(f"{i} * {j} = {i * j}")

sys.stdout = sys.__stdout__

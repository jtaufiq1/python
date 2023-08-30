#!/usr/bin/python3

import random

# Generate random number between low and high
def gen_num():
    low = int(input("Lowest number: "))
    high = int(input("Highest number: "))
    comp_num = random.randint(low,high)
    return comp_num
def pick_num():
    print("I am thinking of a number...")
    num = int(input("Guess the number: "))
    return num
def guess_num():
    comp_num = gen_num()
    isTrue = True
    while isTrue:
        num = pick_num()
        if num == comp_num:
            print("Correct, you win")
            isTrue = False
        elif num < comp_num:
            print("Too low, try again:")
        elif num > comp_num:
            print("Too High, try again:")

guess_num()

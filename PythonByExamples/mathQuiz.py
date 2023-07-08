#!/usr/bin/python3

import random

# MATH QUIZ
# Ask five questions randomly generating two whole numbers
#+ Eg: [num1] + [num2] Get answer from user
# If answer is correct, add a point to their score
# Display number answered correctly out of the five

MAX = 5
score = 0

for i in range(1, MAX+1):
    randNum1 = random.randrange(1,50,3)
    randNum2 = random.randrange(1,100,5)

    ans = int(input(f"{i}) {randNum1} + {randNum2} = "))
    total = randNum1 + randNum2
    if ans == total:
        score = score + 1

print(f"You answered {score} out of {MAX} correctly")

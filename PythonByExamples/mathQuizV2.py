#!/usr/bin/python3

import random
import csv

# SIMPLE MATH QUIZ V2
# Ask the user for their name
# Generate 2 random questions
#+ Eg: [num1] + [num2] Get answer from user
# Store the user's name, the questions asked, their answers
#+ their final score in a csv file
# Append to the csv file anytime the program is runned.

filename = 'quiz_data.csv'
score = 0

# Menu
print("1. Take a Quiz")
print("2. Quiz Data")
print("3. Reset")

# User
name = input("Enter your name: ").lower()

#Quiz Q1
randNum1 = random.randrange(1,50,3)
randNum2 = random.randrange(1,100,5)

q1_ans = int(input(f"1. {randNum1} + {randNum2} = "))
total = randNum1 + randNum2
if q1_ans == total:
    score = score + 1
q1 = str(f'{randNum1} + {randNum2}')

#Quiz Q2
randNum1 = random.randrange(1,50,3)
randNum2 = random.randrange(1,100,5)

q2_ans = int(input(f"2. {randNum1} + {randNum2} = "))
total = randNum1 + randNum2
if q2_ans == total:
    score = score + 1
q2 = str(f'{randNum1}+{randNum2}')

# Store/Append
new_rec = f"{name},{q1},{q1_ans},{q2},{q2_ans},{score}\n"
print(new_rec,end='')

file = open(filename,'a')
file.write(str(new_rec))
file.close()


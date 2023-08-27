#!/usr/bin/python3

import csv

# Comma Separated Values (csv)

csvFile = "stars.csv"
file = open(csvFile, 'a')

name = input("Enter a name: ")
age = int(input("Enter age: "))
month = input("Enter month: ")

newRecord = f"{name},{age},{month}\n"

file.write(str(newRecord))
file.close()

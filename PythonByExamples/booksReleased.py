#!/usr/bin/python3

import csv

# Get start year and end year
# Display all books released in between

start_year = int(input("Start year: "))
end_year = int(input("End year: "))
next_year = 2023 + 1
# Year Constraints
if start_year < 1000:
    print("invalid year")
elif start_year > next_year:
    print(f"Not yet in {start_year}")
elif start_year > end_year:
    print("invalid year")

filename = 'books.csv'
file = tuple(csv.reader(open(filename)))

# released year
for rl in file:
    if int(rl[3]) >= start_year and int(rl[3]) <= end_year:
        print(rl)

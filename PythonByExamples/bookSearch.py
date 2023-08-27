#!/usr/bin/python3
import csv

# Search in books.csv
file = 'books.csv'
books = tuple(csv.reader(open(file)))
term = input("Search: ").lower().strip()

print(f"#\tTitle\tAuthor\tReleased Year")
for row in books:
    if term in str(row):
        print(row[0],row[1].title(),row[2].title(),row[3])

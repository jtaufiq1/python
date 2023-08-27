#!/usr/bin/python3

import csv

file = 'books.csv'
books = list(csv.reader(open(file)))

print(f"No of Books: {len(books)}")

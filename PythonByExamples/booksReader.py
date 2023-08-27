#!/usr/bin/python3
import csv

file = open('books.csv')

reader = csv.reader(file)
rows = tuple(reader)
for row in rows:
    book_no = row[0]
    title = row[1].title()
    author = row[2].title()
    rel_year = row[3]
    print(book_no,title,author,rel_year)

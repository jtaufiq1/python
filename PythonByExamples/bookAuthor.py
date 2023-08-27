#!/usr/bin/python3
import csv

# Search author in books.csv file
file = 'books.csv'
books = tuple(csv.reader(open(file)))
author = input("Author: ").lower().strip()

book_authors = []
for row in books:
    #if author in str(row):
    book_authors.append(row[2])

if len(book_authors) != 0:
    print(f"#\tTitle\tAuthor\tReleased Year")
    for _author in book_authors:
        if author in book_authors:
            print(row[0],row[1].title(),row[2].title(),row[3])
else:
    print(f"{author} not in the book store")

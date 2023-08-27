#!/usr/bin/python3

import csv

# Create books.csv file with books data
# DATA: book no., book title, book author, year released.

book_file = 'book'
books_data = tuple(csv.reader(open(book_file)))
row_no = 0
h_row = '#;'

book = 'books.csv'
csv_file = open(book,'w')

for r in books_data:
    # Skip header row
    if h_row in r:
        row_no = row_no + 1
    else:
        book_no = books_data[row_no][0]
        book_title = books_data[row_no][1]
        book_author = books_data[row_no][2]
        rel_year = books_data[row_no][3]

        book_data = f"{book_no},{book_title},{book_author},{rel_year}\n"
        csv_file.write(str(book_data))
        row_no = row_no + 1

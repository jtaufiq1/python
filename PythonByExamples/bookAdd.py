#!/usr/bin/python3

import csv

# Add N-Books to the books.csv file with new book
# DATA: book no., book title, book author, year released.

no_books = int(input("How many books do you want to add: "))

book = 'books.csv'
book_count = len(list(csv.reader(open(book))))
csv_file = open(book,'a')

for n in range(0,no_books):
    print("Add new book record")
    book_no = book_count
    book_title = input("Book Title: ").lower()
    book_author = input("Book Author: ").lower()
    rel_year = int(input("Release Year: "))

    book_data = f"{book_no},{book_title},{book_author},{rel_year}\n"
    csv_file.write(str(book_data))
    book_count = book_count + 1
csv_file.close()

#!/usr/bin/python3

import csv

filename = "books.csv"
file = list(csv.reader(open(filename)))
tmp_books = []

print("\tBooks in Bookshelf")
for row in file:
    print(row[0],row[1].title(),row[2].title(),row[3])
    tmp_books.append(row)

# Select Book Number
book_no = int(input("Book No.: "))
if book_no >= 0 and book_no < len(tmp_books):
    mod_type = input("Do you want to (d)elete or (m)odify? ").lower()
    if mod_type in ('m','d'):
        if mod_type == 'm':
            print(f"Modify book {book_no}:")
            print("1. Title")
            print("2. Author")
            print("3. Release year")
            res = input(": ")
            if res in ('1','2','3'):
                if res == '1':
                    title = input("Title: ").lower()
                    tmp_books[book_no][1] = title
                elif res == '2':
                    author = input("Author: ").lower()
                    tmp_books[book_no][2] = author
                elif res == '3':
                    rel_yr = int(input("Release year: "))
                    tmp_books[book_no][3] = rel_yr
        elif mod_type == 'd':
            print(f"Deleting '{tmp_books[book_no][1].title()}'", end=' ')
            print(f"by {tmp_books[book_no][2].title()}")
            del tmp_books[book_no]

        # Write changes (Override)
        filename = "books.csv"
        file = open(filename,'w')
        row_no = 0
        for row in tmp_books:
            book_no = row_no
            title = tmp_books[row_no][1]
            author = tmp_books[row_no][2]
            r_year = tmp_books[row_no][3]
            new_book = f"{book_no},{title},{author},{r_year}\n"
            file.write(str(new_book))
            row_no = row_no + 1
        file.close()
    else:
        print("Invalid response")
        print("Exiting...")

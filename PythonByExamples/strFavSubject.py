#!/usr/bin/python3

# Get favorite subject
# Display letter separated with '-'

fav_subject = input("Enter your favorite subject: ")
for l in fav_subject:
    if fav_subject.index(l) == len(fav_subject)-1:
        end_char = '\n'
    else:
        end_char = '-'
    print(l.upper(),end=end_char)

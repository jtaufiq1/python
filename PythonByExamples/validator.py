#!/usr/bin/python3

# Prompt for input of 1,2 or 3
# If input is 1, Output 'Thank you'
# Else if input is 2, Output 'Well done'
# Else if input is 3, Output 'Correct'
# Else, Output 'Error message'

answer = input("Enter [1, 2 or 3]: ")

if answer == "1":
    message = "Thank you"
elif answer == "2":
    message = "Well done"
elif answer == "3":
    message = "Correct"
else:
    message ="Error message"

print(message)

#!/usr/bin/python3

# Display a menu of three choice
# Ask the user for a choice
# If choice is not part of the menu item
#+ Display an error message
#
# If the user selects 1, ask the user to enter school
#+ subjects and save it to a new file 'subjects.txt'
#+ which overrides any existing file with the same name.
#
# If the user selects 2, Display the contents of the file
#+ 'subjects.txt'
#
# If the user selects 3, Ask the user to enter a new subject
#+ then save it and display the entire contents of the file.
#
# RUN SEVERAL TESTS ON THE PROGRAM
def writeln(fn,line):
    line = f"{line}\n"
    fn.write(line)

def append(fn,line):
    writeln(fn,line)

def read(fn):
    print(open(fn,'r').read(),end='')

def menu():
    print("1) Create a new file")
    print("2) Display the file")
    print("3) Append new subject to the file")
    sel = input("Make a selection [1, 2 or 3]: ")
    return sel

fileName = 'subjects.txt'
onMenu = True
while onMenu:
    choice = menu()
    if choice == "1":
        file = open(fileName,'w')
        subject = input("Enter new subject: ").title()
        writeln(file,subject)
        file.close()
    elif choice == "2":
        read(fileName)
    elif choice == "3":
        file = open(fileName,'a')
        subject = input("Append new subject: ").title()
        writeln(file,subject)
        file.close()

        read(fileName)
        onMenu = False
    else:
        print("Invalid selection. Try again...")
        onMenu = False

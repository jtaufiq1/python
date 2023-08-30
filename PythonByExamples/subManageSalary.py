#!/usr/bin/python3

import csv

# Subprogram: Menu items
#             1) Add to file
#             2) View all records
#             3) Quit program
#             -) Add to file
# Subprogram: Add to file
#             Add to a file 'salaries.csv'
#             File stores name and salary
# Subprogram: View all records in file
#             Display all the records in the file
# Keep running until program is quit.

# Menu
def menu_res():
    print("1) Add to file")
    print("2) View all records")
    #print("3) Delete a record")
    print("3) Quit program")

    __OPT_LIST = ('1','2','3')
    option = input("Select an option: ")
    if option in __OPT_LIST:
        return option

def __in__(msg):
    __input = input(f'{msg}: ').lower()
    return __input
def __name():
    __name = __in__('name')
    return __name
def __salary():
    __salary = float(__in__('Salary: '))
    return __salary

# Add to file
def add_salary():
    name = __name()
    salary = __salary()

    filename = 'salary.csv'
    file = open(filename,'a')

    append_rec = f"{name},{salary}\n"
    file.write(append_rec)
    file.close()

def view_salary():
    filename = 'salary.csv'
    file = tuple(csv.reader(open(filename)))
    row_no = 1

    print("\tsalary info".upper())
    for row in file:
        name = row[0].title()
        salary = row[1]
        print(row_no,name,salary)
        row_no = row_no + 1
    print("\t***")

#def delete_salary():
#    filename = 'salary.csv'
#    salary_data = tuple(csv.reader(open(filename)))
#    _tmp_list = []
#    for s in salary_data:
#       _tmp_list.append(s)
#   name = __name()
#   if name _tmp_list:
#       index = _tmp_list.index(name)
#       _tmp_list.remove(name)
#       del _tmp_list[index]

    # Override file
#    file = open(filename,'w')
#    for r in _tmp_list:
#        file.write(f"{row}\n")
#    file.close()

def manage_salary():
    is_running = True
    while is_running:
        opt = menu_res()
        if opt == '1':
            add_salary()
        elif opt == '2':
            view_salary()
        #elif opt == '3':
        #    delete_salary()
        elif opt == '3':
            is_running = False
        else:
            print("Invalid option")

# main
manage_salary()

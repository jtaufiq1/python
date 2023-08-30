#!/usr/bin/python3

import csv

# Subprogram: Menu items
#             1) Add to file
#             2) View all records
#             3) Delete a record
#             4) Quit program
# Subprogram: Add to file
#             Add a record to a file 'salaries.csv'
#             File stores name and salary
# Subprogram: Delete a record from the file
#             Remove a record the file 'salaries.csv'
# Subprogram: View all records in file
#             Display all the records in the file
# Keep running until program is quit.

# Menu
def menu_res():
    print("1) Add to file")
    print("2) View all records")
    print("3) Delete a record")
    print("4) Quit program")

    __OPT_LIST = ('1','2','3','4')
    option = input("Select an option: ")
    if option in __OPT_LIST:
        return option.strip()

def __in__(msg):
    __input = input(f'{msg}: ').lower()
    return __input.strip()
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
    print("No. Name - Salary")
    for row in file:
        name = row[0].title()
        salary = row[1]
        print(f"{row_no}. {name} - {salary}")
        row_no = row_no + 1
    print("\t***")

def delete_salary():
    filename = 'salary.csv'
    salary_data = tuple(csv.reader(open(filename)))
    _tmp_list = []

    name = __name()
    for s in salary_data:
        if name == s[0]:
            #index = _tmp_list.index(name)
            #_tmp_list.remove(name)
            #del _tmp_list[index]
            print(f"{name} deleted")
        else:
            #print(s)
            _tmp_list.append(s)

    # Override file
    file = open(filename,'w')
    for row in _tmp_list:
        _name = row[0]
        _salary = row[1]
        rec = f"{_name},{_salary}\n"
        file.write(rec)
    file.close()

def manage_salary():
    is_running = True
    while is_running:
        opt = menu_res()
        if opt == '1':
            add_salary()
        elif opt == '2':
            view_salary()
        elif opt == '3':
            delete_salary()
        elif opt == '4':
            is_running = False
        else:
            print("Invalid option")

# main
manage_salary()

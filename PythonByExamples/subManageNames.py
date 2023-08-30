#!/usr/bin/python3

# MANAGE NAMES
# Subprogram: menu items
#             1) Add name
#             2) Change name
#             3) Delete name
#             4) View names
#             0) Quit

# Menu
def menu_res():
    print("1) Add name")
    print("2) Change name")
    print("3) Delete name")
    print("4) View names")
    print("0) Quit")

    OPT_LIST = ('1','2','3','4','0')
    option = input("Option: ")
    if option in OPT_LIST:
        return option

# Add name
def _read_name(msg):
    _name = input(f"{msg}: ").lower()
    return _name
def add_to(names):
    name = _read_name('Add name')
    names.append(name)

# Change name
def change_in(names):
    name = _read_name('Change name')
    if name in names:
        index = names.index(name)
        new_name = _read_name('New name')
        names[index] = new_name
        print(f"{name} changed to {new_name}")

# Delete name
def delete_in(names):
    name = _read_name('Delete name')
    if name in names:
        #names.remove(name)
        index = names.index(name)
        del names[index]
        print(f"{name} deleted")

# View names
def view_(names):
    no = 1
    print("\tAll Names".upper())
    for name in names:
        print(no,name.title())
        no = no + 1
    print("\t***")

# Manage Names
def manage_names():
    names = []
    is_run = True
    while is_run:
        opt = menu_res()
        if opt == '1':
            add_to(names)
        elif opt == '2':
            change_in(names)
        elif opt == '3':
            delete_in(names)
        elif opt == '4':
            view_(names)
        elif opt == '0':
            is_run = False
        else:
            print("Invalid option")

# main sub
manage_names()

#!/usr/bin/python3

from tkinter import *
# Get name from user
# Add to the end of name list
# Clear names

# Label
def input_label():
    box_style = 'solid'
    justify = 'center'

    label = Label(text='New Name:')
    label.place(x=10,y=43, height=32)
    label['fg'] = 'white'
    label['bg'] = 'black'

def add_name():
    name = entry.get()
    entry.delete(0,END)

    name = name.strip().lower()
    listbox.insert(0,name)

def clear():
    listbox.delete(0,END)

def del_name():
    print("name deleted from list")

# __main__
window = Tk()
window.title("Name List")
window.geometry('600x350')

# Heading
heading = Label(text='Add name to a list'.title())
heading.place(x=190,y=10)
heading['relief'] = 'groove'
heading['justify'] = 'center'
heading['bg'] = 'black'
heading['fg'] = 'white'

# Input widget
input_label()
entry = Entry()
entry.place(x=85,y=43, height=33,width=200)
entry['justify'] = 'center'
entry['relief'] = 'solid'

# Output widget
listbox = Listbox()
listbox.place(x=86,y=80,width=200)

# Buttons
add_btn = Button(text='Add', command=add_name)
add_btn.place(x=300,y=45)

del_btn = Button(text='Delete', command=del_name)
del_btn.place(x=300,y=75)

clr_btn = Button(text='Clear', command=clear)
clr_btn.place(x=300,y=105)

exit_btn = Button(text='Exit', command=window.destroy)
exit_btn.place(x=300,y=135)

window.mainloop()

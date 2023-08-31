#!/usr/bin/python3

import tkinter as tk
from tkinter import *

window = Tk()
window.title("Drop down list".upper())
window.geometry('450x200')  # Window width and height

label = Label(text = 'Drop Down List')
label.place(x=20,y=10, width=100,height=25)

list_items = Variable(value=('file','edit','format','tools','help'))
list_box = Listbox(listvariable=list_items,height=3)
list_box.place(x=130,y=15, width=100,height=25)
list_box.pack(expand=False,fill=tk.Y)

window.mainloop()

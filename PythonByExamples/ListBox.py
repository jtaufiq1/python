#!/usr/bin/python3

import tkinter as tk
from tkinter import Variable, ttk
from tkinter.messagebox import showinfo

window = tk.Tk()
window.title("Drop down list".upper())
#window.geometry('180x100')  # Window width and height

langs = ('Java','C#','C','C++','Python',
         'Go','Javascript','PHP','Swift')

list_items = Variable(value=langs)
list_box = tk.Listbox(window,
                      listvariable=list_items,
                      selectmode=tk.EXTENDED)
list_box.pack(expand=False,fill=tk.Y,side=tk.LEFT)

scrollbar = ttk.Scrollbar(
    window,
    orient=tk.VERTICAL,
    command=list_box.yview
)
list_box['yscrollcommand'] = scrollbar.set
scrollbar.pack(side=tk.LEFT,expand=True,fill=tk.Y)

# Select callback
def items_selected(event):
    # Get all selected items
    selected_indices = list_box.curselection()
    # Get selected items
    selected_langs = ",".join([list_box.get(i) for i in selected_indices])
    msg = f'You selected: {selected_langs}'
    showinfo(title='Information',message=msg)
list_box.bind('<<ListboxSelect>>', items_selected)

window.mainloop()

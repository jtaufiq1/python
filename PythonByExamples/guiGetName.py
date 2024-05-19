#!/usr/bin/python3

from tkinter import *

# Create a window
root_win = Tk()
root_win.title("Welcome")
root_win.geometry('450x150')

# Setup & Position label and input box
in_label = Label(text="Name:")
in_label.place(x=10,y=16, height=25,width=50)

in_text = Entry()
in_text.place(x=54,y=17, height=25,width=160)

# Output
out_label = Message()
out_label.place(x=55,y=42, height=80,width=158)
out_label['relief'] = 'sunken'

# Click
def click():
    name = in_text.get()
    if name == "":
        out_label['bg'] = 'red'
    else:
        out_label['bg'] = 'green'
        name = f'Hello, {name.title()}'
        out_label['text'] = name
    name_len = len(in_text.get())
    in_text.delete(0,name_len)
click_btn = Button(text='Click',command=click)
click_btn.place(x=214,y=17, height=25,width=60)
click_btn['bg'] = 'blue'
click_btn['fg'] = 'white'

def clear():
    out_label['text'] = ''
    out_label['bg'] = 'white'
clr_btn = Button(text='Clear',command=clear)
clr_btn.place(x=214,y=50, height=25,width=60)
clr_btn['bg'] = 'white'
clr_btn['fg'] = 'red'

exit_btn = Button(text='Exit',command=root_win.destroy)
exit_btn.place(x=214,y=97, height=25,width=60)
exit_btn['bg'] = 'red'
exit_btn['fg'] = 'white'

root_win.mainloop()

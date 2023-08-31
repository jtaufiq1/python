#!/usr/bin/python3

from tkinter import *

window = Tk()
window.title("Window Title")
window.geometry('450x200')  # Window width and height

label = Label(text = 'Enter number:')
label.place(x=20,y=10, width=90,height=20)

window.mainloop()

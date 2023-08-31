#!/usr/bin/python3

from tkinter import *

def call():
    msg = Label(window,text='You pressed the button')
    msg.place(x=30,y=50)
    button['bg'] = "blue"
    button['fg'] = "white"

window = Tk()
window.geometry('250x110')
button = Button(text='Press me',command=call)
button.place(x=40,y=25,width=120,height=25)
window.mainloop()

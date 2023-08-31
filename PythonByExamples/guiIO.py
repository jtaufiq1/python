#!/usr/bin/python3

from tkinter import *
import random

# Button: command
def click():
    COLORS = ['red','blue','green','yellow','white']
    randColor = random.choice(COLORS)

    #btn_click['bg'] = 'blue'
    #btn_click['fg'] = 'white'

    output_box['bg'] = randColor
    output_box['text'] = entry_box.get().upper()

window = Tk()
window.title("GUI IO TEST")
window['bg'] = 'orange'
window.geometry('400x150')  # Window width and height

label = Label(text = 'Enter some text:')
label.place(x=10,y=10, width=100,height=25)
label['bg'] = 'orange'

# Entry: Input box
entry_box = Entry()
entry_box.place(x=110,y=10, width=100,height=25)

# Message: Output box
output_box = Message()
output_box.place(x=110,y=35, width=100,height=50)
output_box['relief'] = 'sunken'

# Button:
btn_click = Button(text = 'Click here', command=click)
btn_click.place(x=110,y=80, width=100,height=25)

window.mainloop()

#!/usr/bin/python3

from tkinter import *
import random

main_win = Tk()
main_win.title("Rolling Dice")
main_win.geometry('450x200')

# Label
label = Label(text='Roll the dice')
label.place(x=180,y=15, height=40,width=100)
label['bg'] = 'green'

# Output
msg_box = Message()
msg_box.place(x=200,y=57, height=45,width=60)

# Button
def roll():
    rand_num = random.randint(1,6)
    msg_box['text'] = rand_num
roll_btn = Button(text='Roll',command=roll)
roll_btn.place(x=200,y=90, height=40,width=60)

main_win.mainloop()

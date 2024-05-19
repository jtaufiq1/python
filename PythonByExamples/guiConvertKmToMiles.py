#!/usr/bin/python3

from tkinter import *

# 1 kilometre = 0.6214 miles
# 1 mile = 1.6093 kilometres
# Get input from user
# Convert between miles and kilometres

# Main window
window = Tk()
window.title("Kilo to miles converter")
window.geometry("300x150")

# Label and entry box
label = Label(text="Miles:")
label.place(x=10,y=10, height=35,width=45)
label['relief'] = "sunken"

entry = Entry()
entry.place(x=50,y=10, height=35,width=80)
entry['relief'] = "sunken"

# Output box
#label['relief'] = "sunken"

window.mainloop()

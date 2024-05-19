#!/usr/bin/python3

from tkinter import *

# Display a number: total = 0
# Get a number from the user
# Add to the total and display the number

# Window
root = Tk()
root.title("Add Number")
root.geometry("400x150")

# Label
label = Label(text="Enter a number:")
label.place(x=10,y=9, height=40,width=100)

# Entry box
total = 0
text = Entry()
text.place(x=110,y=15, height=30,width=65)
text["justify"] = "center"
text["relief"] = "raise"

# Adder
def _add_to(total, num):
    total = total + num
    return total
# Add Button
def btn_add():
    in_text = text.get().strip()
    text_len = len(in_text)

    _WHITE_SPACE = (""," ","\t","\n","\r\n")
    if in_text in _WHITE_SPACE or (not in_text.isdigit()):
        print(f"[Value Error]: not a number")
    else:
        num = int(in_text)
        total = result["text"]

        total = int(total)
        if num < 0 or num > 0:
            total = _add_to(total,num)
            result["text"] = str(total)
    text.delete(0,text_len)
add_btn = Button(text="Add",command=btn_add)
add_btn.place(x=180,y=10, height=40,width=55)

# Reset Button
def btn_reset():
    in_text = text.get()
    text_len = len(in_text)
    text.delete(0,text_len)
    result["text"] = "0"
reset_btn = Button(text="Reset", command=btn_reset)
reset_btn.place(x=240,y=10, height=40,width=55)

# Output
result = Message(text=str(total))
result.place(x=10,y=48, height=50,width=380)
result["bg"] = "grey"
result["relief"] = "sunken"
result["justify"] = "left"

root.mainloop()

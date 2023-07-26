#!/usr/bin/python3

# Enter list of 10 colours
# Get starting number between 0 and 4
# Get an end number between 5 and 9
# Display the list for those colours
#+ between the start and end numbers

colors = [
    'red','blue','green','brown','black',\
    'grey','yellow','pink','white','orange'
]
start_color_num = ('0','1','2','3','4')
end_color_num = ('5','6','7','8','9')

start_number = input("Enter starting number(0-4): ")
end_number = input("Enter end number(5-9): ")

if start_number in start_color_num and end_number in end_color_num:
    print(colors[int(start_number):int(end_number)])
#else:
#    pass
#    print("invalid input")

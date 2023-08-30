#!/usr/bin/python3

import random

# SUBPROGRAM: ADDITION & SUBTRACTION
# Defines subs
# Subprogram: menu items
#             1) Addition
#             2) Subtraction
#             Enter 1 or 2:
# Subprogram: number generator
#             two random numbers between range
# Subprogram: add two random numbers (num1 - num2)
#             numbers range between 5 and 20
#             return user's answer and the correct answer
# Subprogram: subtract two random numbers (num1 - num2)
#             numbers range between 25 and 50
#             return user's answer and the correct answer
# Subprogram: check answers
#             if the answer user's answer matches the correct answer,
#             diplay 'Correct'
#             else display 'Incorrect'
# If incorrect option is selected from the menu, display 'Invalid option'

#def _option_res():
#pass
def menu_res():
    print('1) Addition')
    print('2) Subtraction')

    __OPT_LIST = ('1','2')
    option = input("Option: ")
    if option in __OPT_LIST:
        return option

def _gen_num(r1,r2):
    rand_num = random.randint(r1,r2)
    return rand_num

def _answer():
    user_ans = int(input("Answer: "))
    return user_ans

def add(num1,num2):
    print(f"{num1} + {num2}", end=' ')
    user_ans = _answer()
    correct_ans = num1 + num2
    return (user_ans,correct_ans)

def subtract(num1,num2):
    print(f"{num1} - {num2}", end=' ')
    user_ans = _answer()
    correct_ans = num1 - num2
    return (user_ans,correct_ans)

def check_answer(func,num1,num2):
    user_ans,correct_ans = func(num1,num2)
    if user_ans == correct_ans:
        print('Correct')
    else:
        print('Incorrect')

def main():
    opt = menu_res()
    if opt == '1':
        num1 = _gen_num(1,20)
        num2 = _gen_num(1,20)
        check_answer(add,num1,num2)
    elif opt == '2':
        num1 = _gen_num(25,50)
        num2 = _gen_num(1,25)
        check_answer(subtract,num1,num2)
    else:
        print('Invalid option')

# main
main()

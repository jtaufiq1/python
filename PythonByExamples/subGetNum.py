#!/usr/bin/python3

def get_num():
    num = int(input("Enter a number: "))
    return num
def print_num():
    num = get_num()
    for i in range(1,num+1):
        print(i)

print_num()

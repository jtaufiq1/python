#!/usr/bin/python3

def get_data():
    user_name = input("Enter your name: ")
    user_age = int(input("Enter your age: "))
    user_data = (user_name,user_age)
    return user_data
def message(user_name,user_age):
    if user_age <= 10:
        print("Hi,", user_name.title())
    else:
        print("Hello,",user_name.title())
def main():
    user_name,user_age = get_data()
    message(user_name,user_age)

main()

#!/usr/bin/python3

# Ask the user for a new password
# Enter again to confirm it
# If it matches, Display 'Thank you'
# Else if it matches but incorrect case
#+ Display 'They must be in the same case'
# Else display 'incorrect'

new_passwd = input("Enter new password: ")
confirm_passwd = input("Confirm password: ")

if new_passwd == confirm_passwd:
    print("Thank you")
elif new_passwd.lower() == confirm_passwd.lower():
    print("They must be in the same case")
else:
    print("Incorrect")

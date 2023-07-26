#!/usr/bin/python3

# Set count to 0
# Get name of user to invite
# Display '[name] has now been invited'
# Increase count by one
# Repeat until invitation is finished

print("\tIt's Party time".upper())

count = 0
answer = "y"
message = ""

while answer == "y":
    name = input("invite: ")

    print(f"\t{name.title()} has now been invited")
    count = count + 1

    print("Do you want to invite anyone again?",end='')
    answer = input("[y|n] ")
    answer = answer.lower()

    if count == 1 and answer == 'n':
        message = "person"
    else:
        message = "people"

print("\t", count, message, "will be coming to the party")

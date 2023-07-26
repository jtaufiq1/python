#!/usr/bin/python3

# Get names of 3 people to invite
#+ and store in a list
# Ask for to invite more
# If answer is (y)es, add another name to the list
# If answer is (n)o, display the number of people
#+ invited to the party.
# Repeat until answer is no

print("\tIt's Party time".upper())
count = 0
invitees = []
is_invite = True
while is_invite:
    if count >= 3:
        print("Do you want to invite anyone again?",end='')
        answer = input("[y|n] ")
        answer = answer.lower()

        if answer == "n":
            print(f"List of invited guests: {invitees}")
            print(f"\t{count} people will be coming to the party")
            invitees.clear()
            is_invite = False
            continue
        elif answer != "y":
            continue

    invitee = input("Invite: ")
    invitees.append(invitee.title())
    count = count + 1
    print(f"{invitee.upper()} has been invited")

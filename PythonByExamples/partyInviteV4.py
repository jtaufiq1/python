#!/usr/bin/python3

# Get names of 3 people to invite
#+ and store in a list
# Ask for to invite more
# If answer is (y)es, add another name to the list
# If answer is (n)o, display the number in the list
#+ Display full list of invited guests
#+ Get name of one invitee
#+ Display the position of name in list
#+ Confirm invitation, if answer is no, delete from list
#+  Display list again.
# Repeat until answer is no

# Function: Convert case
def mk_upper(s):
    return str(s).upper()
def mk_lower(s):
    return str(s).lower()
def mk_title(s):
    return str(s).title()

print("\tIt's Party time".upper())
count = 0
invitees = []
is_invite = True

while is_invite:
    if count >= 3:
        print("Do you want to invite anyone again?",end='')
        answer = input("[y|n] ")
        answer = mk_lower(answer)

        if answer == "n":
            print(f"\t{count} people will be invited to the party")
            print(f"{invitees}")

            name = input("Enter a from the list: ")
            name = mk_lower(name)
            if name in invitees:
                print(f"{invitees.index(name)}: {name.upper()}")
                print(f"Do you still want to invite {name.upper()} ", end='')
                answer = input("(Y)es/(N)o: ")
                answer = mk_lower(answer)
                if answer == "n":
                    index = invitees.index(name)
                    #del invitees[index]
                    #invitees.remove(name)
                    invitees.pop(index)
                    print(f"{invitees}")
            is_invite = False
            continue
        elif answer != "y":
            continue

    invitee = input("Invite: ")
    invitees.append(mk_lower(invitee))
    count = count + 1

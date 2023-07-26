#!/usr/bin/python3

# Create a list of TV Programmes(title)
# Display each on a separate line
# Ask the user to enter another show
#+ and insertion point in the list
# Display all the TV Programmes with their positions.

tv_progs = ['talented kids','sports','documentaries','movie hour']

for show in tv_progs:
    print(show.title())

show = input("\nAdd a TV show: ")
pos = int(input("Position in show lists: "))
tv_progs.insert(pos, show)

print("\tTV Programs".upper())
for show in tv_progs:
    print(f"{tv_progs.index(show)}: {show.title()}")

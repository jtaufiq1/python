#!/usr/bin/python3

# Make a list of two sports
# Ask the user for favorite sports
# Append favorite sports to sports lists
# Sort list
# Display sports list

sports_list = ["Tennis","Football"]
while True:
    print("""\tFavourite Sports
      1 - Add to favourite
      2 - Display favourite
      3 - Remove from list
      q - Quit
          """)
    opt = input("Choose an option: ")
    opt = opt.lower()

    if opt == '1':
        fav_sport = input("What's your favourite sport? ")
        sports_list.append(fav_sport.title())
    elif opt == '2':
        sports_list.sort()
        print(f"Favourites sports {sports_list}")
    elif opt == '3':
        fav_sport = input("Enter sport to remove: ")
        fav_sport = fav_sport.title()

        if fav_sport.title() in sports_list:
            sports_list.remove(fav_sport)
        else:
            print(f"{fav_sport} not in list")
    elif opt == 'q':
        print("Quitting...")
        break
    else:
        print("Invalid option")
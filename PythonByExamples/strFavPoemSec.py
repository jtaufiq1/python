#!/usr/bin/python3

# Show the user a line of text
# Ask for start and end point
# Display characters between the points.

fav_poem = "When I was a poor man, my family didn't know me."
print(fav_poem)

start_point = int(input("Section Start: "))
end_point = int(input("Section End: "))

if start_point < 0 or end_point < start_point:
    print("Invalid Section")
else:
    print(fav_poem[start_point:end_point])

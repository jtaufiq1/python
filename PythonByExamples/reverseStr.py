#!/usr/bin/python3

# Get string from user
# Display letters backward
#+ Each on separate line

word = input("Enter a word: ").strip()
word = word.split()[0]
length = len(word)-1
for i in range(length,-1,-1):
    print(word[i])

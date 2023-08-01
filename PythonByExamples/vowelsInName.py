#!/usr/bin/python3

# Ask user for name
# Display number of vowels in name

VOWELS = ('a','e','i','o','u')

name = input("Enter your name: ")
name = name.lower()

vowel_count = 0
for l in name:
    if l in VOWELS:
        vowel_count = vowel_count + 1

if vowel_count > 1:
    vowel = 'vowels'
else:
    vowel = 'vowel'
print(f"You have {vowel_count} {vowel} in your name.")

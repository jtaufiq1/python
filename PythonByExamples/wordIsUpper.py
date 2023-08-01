#!/usr/bin/python3

# Get word in caps
# If all letters not in uppercase
# Repeat until the word is in uppercase

word = input("Enter a word in caps: ").strip()
word = word.split()[0]

isTrue = True
while isTrue:
    #count_caps = 0
    #w_length = len(word)
    #for l in word:
    #    if l.isupper() and count_caps < w_length:
    #        count_caps = count_caps + 1
    #    else:
    #        break
    #DEBUG: print(f"Word {w_length}: All Caps {count_caps}")
    if word.isupper():
        print(word)
        isTrue = False
    else:
        word = input("Try again: ").strip()
        word = word.split()[0]

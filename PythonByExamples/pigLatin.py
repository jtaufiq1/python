#!/usr/bin/python3

# Pig Latin
# Get input of word
# Takes first consonant of word
# Move it to the end and add 'ay'
#
# If first letter of word is vowel
# Add 'way' to the end of the word
# Display new word in lower case letters.

word = input("Enter a word: ")
l = word[0:1]

isVowel = False

if l != 'a' and l != 'e' and l != 'i' and l != 'o' and l != 'u':
    word = word[1:] + l + 'ay'
else:
    word = word + 'way'

print(word.lower())

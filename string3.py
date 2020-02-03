# String methods

name: str = "Python programming"
lang: str = "language"
remarks: str = " is soo simple and clean"

new_name = name.replace("p", "P");
print(new_name)
print("\n")

# Reversed string
new_name2 = "-".join(reversed(lang))
print(new_name2[:]) # Slicing 

sentence = "this word is on a single line"

# Creating list of words
word = sentence.split(" ")

word = word[0].upper()
print(word)
print('\n')

# Join char
word = "-".join(word)
print(word)

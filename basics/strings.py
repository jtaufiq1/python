course = "Python Programming"

print(len(course)) # get length of string

print(course[0]) # prints first char of the string
print(course[-1]) # prints the last char of the string

print(course[0:3]) # prints char from 0 excluding 3
print(course[:3])

print(course[0:]) # print from 0 to the end
print(course[:]) # same as above


# Escape sequences
# \"
# \'
# \\
# \n

# handling quotes
message = "Python message"

# String concatenation
# ... using +
first = "Taufiq"
last = "Gh"
full = first + " " + last

# ... using format string
full = f"{first} {last}"
print(full)
# valid expression can be placed in the curly braces



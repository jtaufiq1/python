# useful string method

# Title formatter v1
def new_line():
    print("\n")

# Title Formatter v2
def title_fmtt(title:str, fmt:str, length:int):    
        print(title.upper())
        print(fmt * length)

# string annotation
course: str = " Python  Programming "

title: str = "string methods"
length = len(title)
format_t = "*"

title_fmtt(title, format_t, length)
new_line()

title = "character case"
length = len(title)
format_t = "-"

title_fmtt(title, format_t, length)
print(course.upper()) # converts to uppercase
print(course.lower()) # converts to lowercase
print(course.title()) # ... first char of every letter to uppercase
new_line()

# trimming white space
title = "trimming whitespace"
length = len(title)

title_fmtt(title, format_t, length)

stripped_course = course.strip()
lstripped = course.lstrip()     # Left spaces
rstripped = course.rstrip()     # Right space

print(stripped_course)
print(lstripped)
print(rstripped)
new_line()

# finding index/substring of a character
# string comparisons are case sensitive
title = "Find index of substring"
length = len(title)

title_fmtt(title, format_t, length)
substring = course.find("Pro")
print("Index of \"Pro\": ",substring)
new_line()

# replace characters
title = "replacing char"
length = len(title)

title_fmtt(title, format_t, length)
r_char = "9"
print(course.replace("P", r_char))
new_line()

# checking for existence of chars
title = "checking existence of chars in string"
length = len(title)

title_fmtt(title, format_t, length)
print("Programming" in course)
print("programming" in course)
new_line()

# inverse check
title = "inverse check"
length = len(title)

title_fmtt(title, format_t, length)
print("Programming" not in course)

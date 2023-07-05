#!/usr/bin/python3

# Quotes and comments

quote_single = 'a string'
quote_double = "a string"
quote_triple = '''a string'''


if quote_single == quote_double:
    print("Single and Double quotes are the same in python")
else:
    print("Single and Double Quotes differ in python")

if quote_triple == quote_single:
    print("Single and Triple quotes are the same to")

if quote_triple == quote_double:
    print("Double and Triple quotes are the same to")

# Sample function with doc
def multilineComment():
    '''
    This is a sample
    Multiline comment
    With triple single quotes
    '''
print(multilineComment.__doc__)

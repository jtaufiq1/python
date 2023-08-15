#!/usr/bin/python3

# Open a file for Writing and Reading
def writeln(f,text):
    #file = open(f,w)
    text = f"{text}\n"
    f.write(text)

# Read Contents of a file
def read(f):
    print(open(f,'r').read(), end='')

# Append to the end of the file
def append(f,text):
    writeln(f,text)

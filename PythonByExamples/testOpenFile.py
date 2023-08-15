#!/usr/bin/python3

# Open a file for Writing and Reading
def writeln(f,text):
    #file = open(f,w)
    text = f"{text}\n"
    f.write(text)
def read(f):
    print(open(f,'r').read(), end='')
def append(f,text):
    writeln(f,text)

fileName = 'countries.txt'
file = open(fileName,'w')
writeln(file,'Ghana')
writeln(file,'Niger')
writeln(file,'Senegal')
writeln(file,'Mali')
file.close()

read(fileName)

file = open(fileName,'a')
text = input("=> Country Name: ")
append(file,text)
file.close()

read(fileName)

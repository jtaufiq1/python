#!/usr/bin/python3

import argparse
import os

# Argumentparser
desc = "File Operation Utility"
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('filename', type=str, help='File name')
parser.add_argument('--create', action='store_true', help='Create a new file')
parser.add_argument('--read', action='store_true', help='Read file content')
parser.add_argument('--update', type=str, help='Update file content')
parser.add_argument('--delete', action='store_true', help='Delete the file')

# Parse arguments (Analyse)
args = parser.parse_args()

# Perform file operation based on argument
filename = args.filename
if args.create:
    # Check for existing file
    # If does not exist, create new
    # Else display "file {filename} exists"
    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            print(f"File {filename} created.")
    else:
        print(f"File {filename} already exist")
elif args.read:
    # Make sure file exists, display file content
    # Else display 'File {filename} does not exist'
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            content = file.read()
            print(f"File '{filename}' content:\n{content}")
    else:
        print(f"File '{filename}' does not exist.")
elif args.update:
    if os.path.exists(filename):
        with open(filename, 'w') as file:
            file.write(args.update)
            print(f"File '{filename}', updated.")
    else:
        print(f"File '{filename}' does not exist.")
elif args.delete:
    if os.path.exists(filename):
        os.remove(filename)
        print(f"File '{filename}' deleted.")
    else:
        print(f"File '{filename}' does not exist.")
else:
    print("Invalid operation: Please use one of the operation flags.")

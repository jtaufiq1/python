#!/usr/bin/python3
# Redirect output to file

import sys

with open('test.txt', 'a') as file:
    sys.stdout = file
    print("Append this to the test file")

# Reset to console
sys.stdout = sys.__stdout__

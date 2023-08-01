#!/usr/bin/python3

# Sample string test

msg = input("Enter some strings: ")
print(f"String length: {len(msg)}")
for l in msg:
    print(l, end="|")

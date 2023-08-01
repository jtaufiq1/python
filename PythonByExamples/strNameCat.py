#!/usr/bin/python3

# Get firstname
# Display length of first name
# Print length of name

first_name = input("Enter your first name: ")
print(f"Length: {len(first_name)}")

surname = input("Enter your surname: ")
print(f"Length: {len(surname)}")

full_name = f"{first_name} {surname}"
print(f"Name: {full_name.upper()}")
print(f"Length: {len(full_name)}")

#!/usr/bin/python3

# Create an empty number list 'nums'
# Get a number from the user
# Add each number to the end of the 'nums' and display it
# If numbers added is 3,
# Ask if last number added should be saved
# If no, remove the last number from the list
# Display the list of numbers

nums = []
for i in range(0,3):
    num = int(input("Enter a number: "))
    nums.append(num)
    print(nums)

print("Do you want to save the last number?")
ans = input("(Y)es or (N)o: ")
ans = ans.lower()

if ans == 'n' or ans == 'no':
    nums.pop()
    print(nums)

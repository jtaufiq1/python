#!/usr/bin/python3

# Binary search algorithm
# Input: Sorted list
# Output: Index of item or special value to denote not found
def binary_search(arr, item):
    first_index = 0
    last_index = len(arr) - 1

    while first_index <= last_index:
        middle_index = (first_index + last_index) // 2

        if arr[middle_index] == item:
            return middle_index

        if arr[middle_index] > item:
            last_index = middle_index - 1
        else:
            first_index = middle_index + 1
    return -1

arr_list = [12,14,20,26,30,40,48]
if binary_search(arr_list, 22) != -1:
    print(f"Found")
else:
    print("Not in list")

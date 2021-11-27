#!/bin/env python3

"""PYTHON COLLECTIONS

LISTS
Ordered and changeable. 
Allows duplicates.
[1, "this", "list", "in", "python"]

"""

thislist = [1, "lists", "in", "python3"]
# print(thislist)

# Indexing
# print(thislist[3])

# Negative Indexing
print(thislist[-1:])
neg_index = thislist[-2:]
print(neg_index)

# Slicing[start:stop].
# Stop not included 
slicelist1 = thislist[1:3]
print("Slice Lists 1: ", slicelist1)

slicelist = thislist[:-2]
print("Slice Lists 2:", slicelist)

# Iterate
for l in thislist:
    print(l)

# Length of list
length = len(thislist)
print("Length of List: ",length)

# Add Items to list
thislist.append("item")
thislist.append("another")

# check item existence in lists
if "item" in thislist:
    print("item exists in ", thislist)

    # Remove Item from list
    thislist.remove("item")
    # Remove the last item/specified index
    thislist.pop()
    # del keyword
    slicelist[1]

    print(thislist)
    print(slicelist)

    # Copy
    newlist1 = list(thislist)
    print(newlist1, len(newlist1))

    # Clear list content
    newlist1.clear()
    print(newlist1)

    # Delete list
    del newlist1
    # print(newlist1)

    newlist2 = thislist.copy()
    print(newlist2)

print("Joining List together")
newlist = slicelist1 + thislist
newlist = thislist.extend(thislist)
print(thislist.count(1))
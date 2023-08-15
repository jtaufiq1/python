#!/usr/bin/python3

# Return item if in the collection
# Else return return none
def checkIn(items, item):
    if item in tuple(items):
        return True
    else:
        return False

sales = {
    'p1':{'N':45,'S':37,'E':54,'W':415},'p2':{'N':62,'S':58,'E':59,'W':304},
    'p3':{'N':78,'S':83,'E':62,'W':501},'p4':{'N':49,'S':47,'E':60,'W':402}
}

# Headings: Regions
regions = ('N','S','E','W')
for r in regions:
    print(f'\t {r}',end='')
print()
print(f"-"*35)

sales_person = sales.keys()
for p in sales_person:
    print(f"{p} |", end=' ')
    #sales_region = sales[p]
    for r in sales[p]:
        print(f"\t{sales[p][r]}",end='')
    print()

# Get name and region
# Display the data
# Get name and region of data to change
# Change the data
# Display the all data for the name
p = input("Enter name of sale person: ")
if checkIn(sales_person, p):
    #r = input("Enter region of sale: ").upper()
    #if checkIn(sales[p].keys(),r):
    #    print(f"{sales[p][r]}")
    # Change Data
    #p = input("Enter name of sale person: ")
    if checkIn(sales_person, p):
        r = input("Enter region of sale: ").upper()
        if checkIn(sales[p].keys(), r):
            newValue = int(input(f"Change data {p} {r}: "))
            sales[p][r] = newValue
            print(sales[p])
    else: pass
else: pass

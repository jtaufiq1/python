#!/usr/bin/python3

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
    sales_region = sales[p]
    for r in sales_region:
        print(f"\t{sales[p][r]}",end='')
    print()

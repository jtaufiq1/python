#!/usr/bin/python3

grades = {
    'std1':{'Ma':45,'En':37,'Fr':54},'std2':{'Ma':62,'En':58,'Fr':59},
    'std3':{'Ma':78,'En':83,'Fr':62},'std4':{'Ma':49,'En':47,'Fr':60}
}

keys = grades['std1'].keys()
for x in keys:
    # Pad with spaces on the first column
    pad = '\t '
    print(f"{pad}{x}",end='')
print()
for k,v in grades.items():
    print(f"{k} {v}")

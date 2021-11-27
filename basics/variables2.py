# variables: Turples, List, Dictionary

python_turple = ('l', 2, 4, 6, 8)
python_list = ['t', 1, 2, 3, 4, 5]
python_dict = {'name':'taufiq gh', 'age':'25', 'town': 'techiman'}

print('turple in python'.upper())
print(python_turple)
for t in python_turple:
    print(t)

# print(python_turple[0])
print('\n')

print('list in python'.upper())
print(python_list)

for l in python_list:
    print(l)

# print(python_list[2])
print('\n')

print('dictionary in python'.upper())
print(python_dict)
for d in python_dict:
    value = python_dict[d]
    print(value.title())
    
    
print('\n')

print('hashed value'.upper())
hash_var = python_dict['town']
print(hash(hash_var))

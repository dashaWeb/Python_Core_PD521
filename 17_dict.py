stud = {
    'name': "Pavlo",
    'surname': "Bondar",
    'age': 18,
    'group': "PD521",
    'marks': [10, 11, 12, 10]
}


def printStudents(student):
    print("="*50)
    print('Name    :: ', student['name'])
    print('Surname :: ', student['surname'])
    print('Age     :: ', student['age'])
    print('Group   :: ', student['group'])
    print('Marks   :: ', student['marks'])
    if 'date' in stud:
        print('Date    :: ', student['date'])

    print("="*50)


print(stud['name'])
print(len(stud))
stud['age'] = 19
print(stud['age'])
# print(stud['age2'])
# print(stud.get('marks'))
printStudents(stud)

print(stud.setdefault('name'))
stud.update([('name', 'Ivan'), ('surname', 'Melnuk'), ('date', '24/05/2000')])
printStudents(stud)
print(stud['date'])
print()
stud['phone'] = '+38(097) - 452 - 12 - 23'
print(stud)

# Delete
del stud['phone']
print(stud)
stud.pop('date')
print(stud)
# stud.popitem()
# print(stud)

for i in stud.keys():
    print(i, end='\t')
print()
for i in stud.values():
    print(i, end='\t')
print()
for key, val in stud.items():
    print(key, val)

clone = stud.copy()
print('Before')
print('Origin')
printStudents(stud)
print('Clone')
printStudents(clone)


print('After')
clone['name'] = 'Stepan'
clone['marks'] = stud['marks'].copy()
clone['marks'][0] = 333
print('Origin')
printStudents(stud)
print('Clone')
printStudents(clone)


group = [
    {'name': "Ivan",
     'age': 15},
    {'name': "Pavlo",
     'age': 16},
    {'name': "Denis",
     'age': 17},
    {'name': "alex",
     'age': 16},
]
for student in group:
    for key, val in student.items():
        print(key, ":", val)
    print('-'*50)

res = list(filter(lambda x: x['age'] >= 16, group))
print(res)
def upAge(x):
    x['age'] = x['age'] + 1
    return x
res = list(map(upAge, group))
print(res)

print(sorted(group, key=lambda x: x['age']))
print(sorted(group, key=lambda x: x['name'].upper()))


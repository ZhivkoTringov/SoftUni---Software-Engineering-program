courses = {}
command = input()
while command != 'end':
    data = command.split(' : ')
    course = data[0]
    name = data[1]
    if course not in courses:
        courses[course] = []
        courses[course].append(name)
    elif course in courses:
        courses[course].append(name)
    command = input()
for key, value in courses.items():
    print(f'{key}: {len(value)}')
    for x in value:
        print(f'-- {"".join([y for y in x])}')
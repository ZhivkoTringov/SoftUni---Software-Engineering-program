students = {}
command = input()
while ":" in command:
    info = command.split(':')
    name = info[0]
    id = info[1]
    course = info[2]
    if course not in students:
        students[course] = {}
    students[course][id] = name
    command = input()
course = ' '.join(command.split('_'))
for key, value in students.items():
    if key == course:
        for id, name in value.items():
            print(f'{name} - {id}')
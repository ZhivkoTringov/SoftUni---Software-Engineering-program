info = {}
command = input()
while command != 'End':
    data = command.split(' -> ')
    company = data[0]
    employee = data[1]
    if company not in info:
        info[company] = []
        info[company].append(employee)
    elif company in info:
        if employee not in info[company]:
            info[company].append(employee)
        else:
            pass
    command = input()
for key, value in info.items():
    print(f'{key}')
    for x in value:
        print(f'-- {"".join([y for y in x])}')
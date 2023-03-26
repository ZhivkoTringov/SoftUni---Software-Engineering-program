parking = {}
num = int(input())
for number in range(num):
    command = input().split(' ')
    data = command[0]
    if data == 'register':
        name = command[1]
        licence_plate = command[2]
        if name not in parking:
            parking[name] = licence_plate
            print(f'{name} registered {licence_plate} successfully')
        elif name in parking and parking[name] != licence_plate or parking[name] == licence_plate:
            print(f'ERROR: already registered with plate number {parking[name]}')
    elif data == 'unregister':
        name = command[1]
        if name not in parking:
            print(f'ERROR: user {name} not found')
        else:
            parking.pop(name)
            print(f'{name} unregistered successfully')
for key, value in parking.items():
    print(f'{key} => {value}')
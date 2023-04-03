from collections import deque

quantity_of_water = int(input())
my_queue = deque()
names = input()
while True:
    if names == 'Start':
        break
    else:
        my_queue.append(names)
    names = input()
command = input()
while command != 'End':
    if 'refill' in command:
        new = command.split()
        quantity_of_water += int(new[1])
    else:
        litters = int(command)
        if litters > quantity_of_water:
            if my_queue:
                print(f'{my_queue.popleft()} must wait')
        else:
            if my_queue:
                quantity_of_water -= litters
                print(f'{my_queue.popleft()} got water')
    command = input()
print(f'{quantity_of_water} liters left')
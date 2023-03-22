num_wagons = int(input())
train = [0] * num_wagons

while True:
    command = input()
    if command == 'End':
        break
    tasks = command.split(' ')
    current_command = tasks[0]
    if current_command == 'add':
        num_people = tasks[1]
        train[-1] += int(num_people)
    elif current_command == 'insert':
        index = int(tasks[1])
        num_people = int(tasks[2])
        train[index] += num_people
    elif current_command == 'leave':
        index = int(tasks[1])
        num_people = int(tasks[2])
        train[index] -= num_people
print(train)
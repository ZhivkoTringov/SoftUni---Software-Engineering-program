gifts = input().split(' ')
while True:
    command = input()
    if command == 'No Money':
        break
    new_commands = command.split(' ')
    if 'OutOfStock' in new_commands:
        for ingredient in range(len(gifts)):
            if new_commands[1] in gifts[ingredient]:
                gifts[ingredient] = 'None'
            else:
                continue
    if 'Required' in new_commands:
        index = int(new_commands[2])
        for i in range(len(gifts)):
            if i == int(new_commands[2]):
                gifts[i] = new_commands [1]
    if 'JustInCase' in new_commands:
        gifts = gifts[:-1]
        gifts.append(new_commands[1])
while 'None' in gifts:
    gifts.remove('None')

print(*gifts, sep=' ')

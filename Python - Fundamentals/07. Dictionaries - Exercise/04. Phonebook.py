phonebook = {}
command = input()
while '-' in command:
    data = command.split('-')
    name = data[0]
    phone_number = data[1]
    if name not in phonebook:
        phonebook[name] = phone_number
    command = input()
for i in range(int(command)):
    names = input()
    if names not in phonebook.keys():
        print(f'Contact {names} does not exist.')
    else:
        print(f'{names} -> {phonebook[names]}')

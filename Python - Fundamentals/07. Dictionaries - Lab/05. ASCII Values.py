command = input().split(', ')
ascii_dict = {command: ord(command) for command in command}
print(ascii_dict)
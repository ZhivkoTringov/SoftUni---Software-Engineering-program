data = input()
emoji = []
for i in range(len(data)):
    if data[i] == ':':
        emoji.append(data[i:i+2])
print('\n'.join(emoji))



data = input()
text = ''
strength = 0
for index in range(len(data)):
    if strength > 0 and data[index] != '>':
        strength -= 1
    elif data[index] == '>':
        strength += int(data[index + 1])
        text += data[index]
    else:
        text += data[index]
print(text)
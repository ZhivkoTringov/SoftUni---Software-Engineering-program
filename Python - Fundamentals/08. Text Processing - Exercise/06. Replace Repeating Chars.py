data = input()
new = []
for i in range(0, len(data)+1):
    if i+2 > len(data):
        new.append(data[-1])
        break
    else:
        if data[i] != data[i+1]:
            new.append(data[i])
        else:
            continue
print(''.join(new))
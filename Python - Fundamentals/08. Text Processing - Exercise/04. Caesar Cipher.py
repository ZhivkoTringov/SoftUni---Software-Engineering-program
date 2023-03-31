data = input()
new_text = []
for i in data:
    new_text.append(ord(i) + 3)
for j in new_text:
    print(''.join(chr(j)), end='')
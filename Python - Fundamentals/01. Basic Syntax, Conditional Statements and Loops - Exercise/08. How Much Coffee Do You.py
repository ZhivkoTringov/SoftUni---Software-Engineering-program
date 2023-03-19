event = ''
counter = 0
while event.lower() != 'end':
    event = input()
    if event.lower() == 'coding' or event.lower() =='dog' or event.lower() =='cat' or event.lower() =='movie':
        if event.islower():
            counter += 1
        else:
            counter += 2
if counter > 5:
    print('You need extra sleep')
else:
    print(counter)
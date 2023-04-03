from collections import deque
name = deque()
people = input()
while True:

    if people == 'End':
        print(f'{len(name)} people remaining.')
        break
    elif people == 'Paid':
        for i in range(len(name)):
            print(name.popleft())
    else:
        name.append(people)
    people = input()

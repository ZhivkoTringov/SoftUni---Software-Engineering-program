while True:
    name = input()
    if name == 'End':
        break
    elif name == 'SoftUni':
        continue
    else:
        for ch in name:
            result = ch*2
            print(result, end='')
        print()
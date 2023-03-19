num = int(input())
for i in range(num):
    name = input()
    if '_' in name or '.' in name or ',' in name:
        print(f'{name} is not pure!')
    else:
        print(f'{name} is pure.')
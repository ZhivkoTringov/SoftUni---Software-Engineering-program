num1 = int(input())
num2 = int(input())
magic_num = int(input())
combination = 0
condition = False
for i in range (num1, num2 + 1):
    for j in range (num1, num2 + 1):
        combination += 1
        if magic_num == i + j:
            print(f'Combination N:{combination} ({i} + {j} = {magic_num})')
            condition = True
            break
    if condition:
        break
if not condition:
    print(f'{combination} combinations - neither equals {magic_num}')


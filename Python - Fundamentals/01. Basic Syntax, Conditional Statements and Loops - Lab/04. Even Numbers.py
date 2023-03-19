num = int(input())
for _ in range(num):
    current_num = int(input())
    if not current_num % 2 == 0:
        print(f'{current_num} is odd!')
        break
else:
    print('All numbers are even.')
num = int(input())
for i1 in range(1, 10):
    for i2 in range(1, 10):
        for i3 in range(1, 10):
            for i4 in range(1, 10):
                if num % i1 == 0 and num % i2 == 0 and num % i3 == 0 and num % i4 == 0:
                    print(f'{int(i1)}{int(i2)}{int(i3)}{int(i4)}', end=' ')
a, b, c = int(input()), int(input()), int(input())
sum_total_seconds = a + b + c
minutes = sum_total_seconds % 60
hours = sum_total_seconds // 60
if minutes < 10:
    print(f'{hours}:{minutes:02d}')
else:
    print(f'{hours}:{minutes}')
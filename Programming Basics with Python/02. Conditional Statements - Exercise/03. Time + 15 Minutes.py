hours = int(input())
minutes = int(input())
all_time = hours * 60 + minutes + 15
hours = all_time // 60
minutes = all_time % 60
if hours > 23:
    print(f'0:{minutes:02d}')
else:
    print(f'{hours}:{minutes:02d}')

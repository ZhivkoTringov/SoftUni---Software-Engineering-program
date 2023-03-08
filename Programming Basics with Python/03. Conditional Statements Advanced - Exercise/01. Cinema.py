type_of_projection = input()
rows = int(input())
columns = int(input())
income = 0
if type_of_projection == 'Premiere':
    income = rows * columns * 12
elif type_of_projection == 'Normal':
    income = rows * columns * 7.5
elif type_of_projection == 'Discount':
    income = rows * columns * 5
print(f'{income:.2f} leva')
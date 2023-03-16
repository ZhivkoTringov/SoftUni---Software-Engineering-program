floors = int(input())
apartment_per_floor = int(input())
apartment_name = ''
apartment_number = 0
for floor in range(floors, 0, -1):
    for n in range(apartment_per_floor):
        apartment_number = 10 * floor + n
        if floor == floors:
            apartment_name = f'L{apartment_number} '
        elif floor % 2 != 0:
            apartment_name = f'A{apartment_number} '
        elif floor % 2 == 0:
            apartment_name = f'O{apartment_number} '
        print(f'{apartment_name}', end='')
    print()
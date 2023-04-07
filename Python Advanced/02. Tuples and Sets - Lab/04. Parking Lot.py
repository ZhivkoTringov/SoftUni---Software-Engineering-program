nums = int(input())
parking = set()
for _ in range(nums):
    direction, car_number = input().split(', ')
    if direction == 'IN':
        parking.add(car_number)
    elif direction == 'OUT':
        parking.remove(car_number)
if parking:
    for num in parking:
        print(num)
else:
    print('Parking Lot is Empty')
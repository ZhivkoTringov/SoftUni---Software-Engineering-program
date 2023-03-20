fire_cells = input().split('#')
water = int(input())
total_fire = 0
effort = 0
cells = []
put_out_fire = []
for i in fire_cells:
    fire = i.split(' = ')
    type_of_fire = fire[0]
    range_of_fire = fire[1]
    if water < int(range_of_fire):
        continue
    else:
        if type_of_fire == 'High' and 81 <= int(range_of_fire) <= 125:
            water -= int(range_of_fire)
            effort += 0.25 * int(range_of_fire)
            total_fire += int(range_of_fire)
            put_out_fire.append(int(range_of_fire))
            cells.append(int(range_of_fire))
        elif type_of_fire == 'Medium' and 51 <= int(range_of_fire) <= 80:
            water -= int(range_of_fire)
            effort += 0.25 * int(range_of_fire)
            total_fire += int(range_of_fire)
            put_out_fire.append(int(range_of_fire))
            cells.append(int(range_of_fire))
        elif type_of_fire == 'Low' and 1 <= int(range_of_fire) <= 50:
            water -= int(range_of_fire)
            effort += 0.25 * int(range_of_fire)
            total_fire += int(range_of_fire)
            put_out_fire.append(int(range_of_fire))
            cells.append(int(range_of_fire))
print(f'Cells:')
for j in cells:
    print(f' - {j}')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')
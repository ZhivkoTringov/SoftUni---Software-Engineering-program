quantity = int(input())
days_to_christmas = int(input())
ornament_set = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15
day_counter = 0
points = 0
total = 0
days = days_to_christmas + day_counter
while True:
    if days_to_christmas == 0:
        break
    days_to_christmas -= 1
    day_counter += 1
    if day_counter % 11 == 0:
        quantity += 2
    if day_counter % 10 == 0:
        points -= 20
        total += tree_skirt + tree_garland + tree_lights
    if day_counter % 2 == 0:
        total += ornament_set * quantity
        points += 5
    if day_counter % 3 == 0:
        total += tree_skirt * quantity + tree_garland * quantity
        points += 13
    if day_counter % 5 == 0:
        total += tree_lights * quantity
        points += 17
        if day_counter % 3 == 0:
            points += 30
if days % 10 == 0:
    points -= 30
print(f'Total cost: {total}')
print(f'Total spirit: {points}')
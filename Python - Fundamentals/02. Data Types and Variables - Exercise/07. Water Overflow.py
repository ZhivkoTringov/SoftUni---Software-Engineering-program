num_of_lines = int(input())
capacity = 255
total_litters = 0
for i in range(num_of_lines):
    litters_of_water = int(input())
    total_litters += litters_of_water
    if total_litters > capacity:
        total_litters -= litters_of_water
        print('Insufficient capacity!')
        continue
print(total_litters)
width_free_space = int(input())
length_free_space = int(input())
height_free_space = int(input())
free_space = width_free_space * length_free_space * height_free_space
occupied_space = 0
while free_space >= occupied_space:
    num_boxes = input()
    if num_boxes == 'Done':
        print(f'{abs(free_space - occupied_space)} Cubic meters left.')
        break
    occupied_space += int(num_boxes)
if occupied_space >= free_space:
    print(f'No more free space! You need {abs(free_space - occupied_space)} Cubic meters more.')

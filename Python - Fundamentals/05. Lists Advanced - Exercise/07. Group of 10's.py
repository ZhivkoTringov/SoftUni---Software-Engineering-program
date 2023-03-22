numbers = list(map(int, input().split(', ')))
starting_index = 0
index = 1

while numbers:
    final_index = int(f'{index}0')
    current_list = [num for num in numbers if num in range(starting_index, final_index + 1)]
    numbers = [number for number in numbers if number not in current_list]
    print(f"Group of {final_index}'s: {current_list}")
    final_index = starting_index
    index += 1
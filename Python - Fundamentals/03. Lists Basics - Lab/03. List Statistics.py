num = int(input())
first_list = []
second_list = []
counter = 0
total = 0
for _ in range(num):
    current_integer = int(input())
    if current_integer >= 0:
        first_list.append(current_integer)
        counter += 1
    else:
        second_list.append(current_integer)
        total += int(current_integer)
print(first_list)
print(second_list)
print(f'Count of positives: {counter}')
print(f'Sum of negatives: {total}')
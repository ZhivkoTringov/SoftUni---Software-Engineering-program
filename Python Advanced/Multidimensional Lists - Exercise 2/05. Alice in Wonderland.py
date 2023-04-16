def get_next_pos(direction, row, col):
    if direction == 'up':
        return row - 1, col
    if direction == 'down':
        return row + 1, col
    if direction == 'left':
        return row, col - 1
    if direction == 'right':
        return row, col + 1


size = int(input())
matrix = []
alice_row = 0
alice_col = 0
total_tea = 0

for row in range(size):
    element = input().split()
    matrix.append(element)

    for col in range(size):
        if element[col] == 'A':
            alice_row = row
            alice_col = col
            element[col] = '*'
            break

current_row, current_col = alice_row, alice_col
while total_tea < 10:
    command = input()
    next_row, next_col = get_next_pos(command, current_row, current_col)
    if not (0 <= next_row < size and 0 <= next_col < size):
        break
    current_row, current_col = next_row, next_col

    if matrix[next_row][next_col] == '.':
        matrix[next_row][next_col] = '*'

    elif matrix[next_row][next_col].isdigit():
        total_tea += int(matrix[next_row][next_col])
        matrix[next_row][next_col] = '*'

    elif matrix[next_row][next_col] == 'R':
        matrix[next_row][next_col] = '*'
        break

if total_tea < 10:
    print("Alice didn't make it to the tea party.")
else:
    print('She did it! She went to the party.')
for roww in matrix:
    print(' '.join(roww))

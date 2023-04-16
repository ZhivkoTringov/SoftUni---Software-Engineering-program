def get_next_pos(position, row, col, steps):
    if position == 'up':
        return row - steps, col
    if position == 'down':
        return row + steps, col
    if position == 'left':
        return row, col - steps
    if position == 'right':
        return row, col + steps


def is_outside(row, col, size):
    return row < 0 or col < 0 or row >= size or col >= size


size = 5
matrix = []
shooter_row = 0
shooter_col = 0
total_targets = 0
for row in range(size):
    data = input().split()
    matrix.append(data)

    for col in range(size):
        if data[col] == 'A':
            shooter_row = row
            shooter_col = col
        if data[col] == 'x':
            total_targets += 1
remaining_targets = total_targets
n = int(input())
path = []
for _ in range(n):
    command_args = input().split()
    command = command_args[0]
    direction = command_args[1]
    if command == 'move':
        steps = int(command_args[2])
        next_row, next_col = get_next_pos(direction, shooter_row, shooter_col, steps)

        if is_outside(next_row, next_col, size) or matrix[next_row][next_col] != '.':
            continue

        matrix[shooter_row][shooter_col] = '.'
        shooter_row, shooter_col = next_row, next_col
        matrix[shooter_row][shooter_col] = 'A'
    else:
        bullet_row, bullet_col = shooter_row, shooter_col
        while True:
            bullet_row, bullet_col = get_next_pos(direction, bullet_row, bullet_col, 1)
            if is_outside(bullet_row, bullet_col, size):
                break
            if matrix[bullet_row][bullet_col] == 'x':
                remaining_targets -= 1
                path.append([bullet_row, bullet_col])
                matrix[bullet_row][bullet_col] = '.'
                break
        if remaining_targets == 0:
            break

if remaining_targets == 0:
    print(f'Training completed! All {total_targets} targets hit.')
else:
    print(f'Training not completed! {remaining_targets} targets left.')

for i in path:
    print(i)

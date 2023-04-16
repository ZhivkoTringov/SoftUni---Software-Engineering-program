def invalid_input(row, col, rows, cols):
    return row < 0 or col < 0 or row > rows or col > cols


rows, cols = [int(x) for x in input().split()]
matrix = []

for _ in range(rows):
    matrix.append(input().split())

while True:
    command = input()
    if command == 'END':
        break
    args = command.split()
    if len(args) != 5 or args[0] != 'swap':
        print('Invalid input!')
        continue

    row1, col1, row2, col2 = [int(x) for x in args[1:]]
    if invalid_input(row1, col1, rows, cols) or invalid_input(row2, col2, rows, cols):
        print('Invalid input!')
        continue

    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
    for row in matrix:
        print(*row, sep=' ')
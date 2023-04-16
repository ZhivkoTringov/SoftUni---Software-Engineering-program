def invali_idx(row, col, rowss):
    return row < 0 or col < 0 or row >= rowss or col >= rowss


rows = int(input())
matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

while True:
    command = input().split()
    if command[0] == 'END':
        break

    elif command[0] == 'Add':
        row1, col1, quantity = [int(x) for x in command[1::]]
        if invali_idx(row1, col1, rows):
            print('Invalid coordinates')
            continue
        matrix[row1][col1] += quantity

    elif command[0] == 'Subtract':
        row1, col1, quantity = [int(x) for x in command[1::]]
        if invali_idx(row1, col1, rows):
            print('Invalid coordinates')
            continue
        matrix[row1][col1] -= quantity
for i in matrix:
    print(' '.join([str(x) for x in i]))
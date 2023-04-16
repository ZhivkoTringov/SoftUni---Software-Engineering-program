def is_knight(row, col, matrix):
    return matrix[row][col] == 'K'


def is_inside(row, col, n):
    return 0 <= row < n and 0 <= col < n


def get_attack_counter(row, col, matrix):
    result = 0
    # rol, col
    # row -2, col -1
    if is_inside(row - 2, col - 1, len(matrix)) and is_knight(row - 2, col - 1, matrix):
        result += 1
        # row -2, col 1
    if is_inside(row - 2, col + 1, len(matrix)) and is_knight(row - 2, col + 1, matrix):
        result += 1
    # row -1, col -2
    if is_inside(row - 1, col - 2, len(matrix)) and is_knight(row - 1, col - 2, matrix):
        result += 1
    # row -1, col 2
    if is_inside(row - 1, col + 2, len(matrix)) and is_knight(row - 1, col + 2, matrix):
        result += 1
    # row 1, col -2
    if is_inside(row + 1, col - 2, len(matrix)) and is_knight(row + 1, col - 2, matrix):
        result += 1
    # row 1, col 2
    if is_inside(row + 1 , col + 2, len(matrix)) and is_knight(row + 1, col + 2, matrix):
        result += 1
    # row 2, col -1
    if is_inside(row + 2, col - 1, len(matrix)) and is_knight(row + 2, col - 1, matrix):
        result += 1
    # row 2, col 1
    if is_inside(row + 2, col + 1, len(matrix)) and is_knight(row + 2, col + 1, matrix):
        result += 1
    return result


n = int(input())

matrix = []

for _ in range(n):
    matrix.append(list(input()))

removed_knights = 0

while True:
    table = {}

    for row in range(n):
        for col in range(n):
            if matrix[row][col] == '0':
                continue
            counter = get_attack_counter(row, col, matrix)
            if counter:
                table[(row, col)] = counter
    if len(table) == 0:
        break

    best_counter = 0
    knight_row, knight_col = 0, 0
    for horse, counter in table.items():
        if counter > best_counter:
            best_counter = counter
            knight_row = horse[0]
            knight_col = horse[1]

    matrix[knight_row][knight_col] = "0"
    removed_knights += 1
print(removed_knights)
def get_new_position(direction, row, col):
    if direction == 'up':
        return row - 1, col
    if direction == 'down':
        return row + 1, col
    if direction == 'left':
        return row, col - 1
    if direction == 'right':
        return row, col + 1

num_of_presents = int(input())
size = int(input())
matrix = []
santa_row = 0
santa_col = 0
total_good_kids = 0
delivered_good_kids = 0
for row in range(size):
    data = input().split()
    matrix.append(data)

    for col in range(size):
        if data[col] == 'S':
            santa_row = row
            santa_col = col
        if data[col] == 'V':
            total_good_kids += 1

while True:
    command = input()
    if command == 'Christmas morning':
        break
    matrix[santa_row][santa_col] = '-'
    santa_row, santa_col = get_new_position(command, santa_row, santa_col)

    if matrix[santa_row][santa_col] == 'V' and num_of_presents:
        num_of_presents -= 1
        delivered_good_kids += 1
        matrix[santa_row][santa_col] = '-'
    elif matrix[santa_row][santa_col] == 'C':
        if matrix[santa_row][santa_col - 1] == 'V' and num_of_presents:
            num_of_presents -= 1
            delivered_good_kids += 1
            matrix[santa_row][santa_col - 1] = '-'
        elif matrix[santa_row][santa_col - 1] == 'X' and num_of_presents:
            num_of_presents -= 1
            matrix[santa_row][santa_col - 1] = '-'
        if matrix[santa_row][santa_col + 1] == 'V' and num_of_presents:
            num_of_presents -= 1
            delivered_good_kids += 1
            matrix[santa_row][santa_col + 1] = '-'
        elif matrix[santa_row][santa_col + 1] == 'X' and num_of_presents:
            num_of_presents -= 1
            matrix[santa_row][santa_col + 1] = '-'
        if matrix[santa_row - 1][santa_col] == 'V' and num_of_presents:
            num_of_presents -= 1
            delivered_good_kids += 1
            matrix[santa_row - 1][santa_col] = '-'
        elif matrix[santa_row - 1][santa_col] == 'X' and num_of_presents:
            num_of_presents -= 1
            matrix[santa_row - 1][santa_col] = '-'
        if matrix[santa_row + 1][santa_col] == 'V' and num_of_presents:
            num_of_presents -= 1
            delivered_good_kids += 1
            matrix[santa_row + 1][santa_col] = '-'
        elif matrix[santa_row + 1][santa_col] == 'X' and num_of_presents:
            num_of_presents -= 1
            matrix[santa_row + 1][santa_col] = '-'

    matrix[santa_row][santa_col] = 'S'

    if num_of_presents == 0 or delivered_good_kids == total_good_kids:
        break
if num_of_presents == 0 and delivered_good_kids < total_good_kids:
    print(f'Santa ran out of presents!')
for row in matrix:
    print(*row, sep=' ')

if delivered_good_kids == total_good_kids:
    print(f'Good job, Santa! {total_good_kids} happy nice kid/s.')
else:
    print(f'No presents for {total_good_kids - delivered_good_kids} nice kid/s.')
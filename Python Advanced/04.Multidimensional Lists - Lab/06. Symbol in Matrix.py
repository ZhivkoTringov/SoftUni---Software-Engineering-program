rows = int(input())
cols = rows
matrix = []
position =[]
for _ in range(rows):
    matrix.append(list(input()))
searched_symbol = input()
found = False

for row_idx in range(rows):
    for col_idx in range(rows):
        if searched_symbol == matrix[row_idx][col_idx]:
            position = [row_idx, col_idx]
            found = True
            break
    if found:
        break
if position:
    print(f'{tuple(position)} ')
else:
    print(f'{searched_symbol} does not occur in the matrix')
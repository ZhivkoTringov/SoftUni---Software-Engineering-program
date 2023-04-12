import sys

rows, cols = [int(el) for el in input().split(', ')]
matrix = []
sub_matrix = []
max_sum_sub_matrix = -sys.maxsize

for _ in range(rows):
    matrix.append([int(el) for el in input().split(', ')])
for row in range(rows - 1):
    for col in range(cols - 1):
        current_matrix = [matrix[row][col], matrix[row][col + 1], matrix[row +1][col], matrix[row + 1][col + 1]]
        current_sum = sum(current_matrix)
        if current_sum > max_sum_sub_matrix:
            max_sum_sub_matrix = current_sum
            sub_matrix = current_matrix.copy()

print(f'{sub_matrix[0]} {sub_matrix[1]}')
print(f'{sub_matrix[2]} {sub_matrix[3]}')
print(max_sum_sub_matrix)
import sys

rows, cols = [int(x) for x in input().split()]

matrix = []
biggest_sum_matrix = []
biggest_sum = -sys.maxsize

for _ in range(rows):
    matrix.append([int(el) for el in input().split()])

for row in range(rows - 2):
    for col in range(cols - 2):
        first_row = [matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]]
        second_row = [matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]]
        third_row = [matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]
        current_matrix = [first_row, second_row, third_row]
        current_sum = sum(first_row) + sum(second_row) + sum(third_row)
        if current_sum > biggest_sum:
            biggest_sum = current_sum
            biggest_sum_matrix = current_matrix.copy()
print(f'Sum = {biggest_sum}')
print(f'{" ".join([str(x) for x in biggest_sum_matrix[0]])}')
print(f'{" ".join([str(x) for x in biggest_sum_matrix[1]])}')
print(f'{" ".join([str(x) for x in biggest_sum_matrix[2]])}')


n = int(input())
matrix = []
primary_diagonal_sum = 0
secondary_diagonal_sum = 0
absolute_sum = abs(primary_diagonal_sum - secondary_diagonal_sum)
for row in range(n):
    matrix.append([int(el) for el in input().split()])
    primary_diagonal_sum += matrix[row][row]
    secondary_diagonal_sum += matrix[row][n - 1 - row]
absolute_sum = abs(primary_diagonal_sum - secondary_diagonal_sum)
print(absolute_sum)
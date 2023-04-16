n = int(input())
matrix = []
for _ in range(n):
    matrix.append([int(el) for el in input().split(', ')])

primary_diagonal = []
secondary_diagonal = []

for row in range(n):
    primary_diagonal.append(matrix[row][row])
    secondary_diagonal.append(matrix[row][n - 1 - row])
if primary_diagonal:
    print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
if secondary_diagonal:
    print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")

rows = int(input())
matrix = []

for _ in range(rows):
    el = [int(x) for x in input().split()]
    matrix.append(el)

diagonal = 0
for i in range(rows):
    diagonal += matrix[i][i]
print(diagonal)
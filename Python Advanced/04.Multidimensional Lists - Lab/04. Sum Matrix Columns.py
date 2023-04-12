rows, cols = [int(el) for el in input().split(', ')]

matrix = []
total = 0
for _ in range(rows):
    element = [int(x) for x in input().split()]
    matrix.append(element)

for col in range(cols):
    res = 0
    for row in range(rows):
        res += (matrix[row][col])
    print(res)
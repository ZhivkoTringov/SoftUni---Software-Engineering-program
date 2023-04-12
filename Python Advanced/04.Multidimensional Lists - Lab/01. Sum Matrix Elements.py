rows, cols = [int(el) for el in input().split(', ')]
matrix = []
total_sum = 0

for _ in range(rows):
    nums = [int(el) for el in input().split(', ')]
    total_sum += sum(nums)
    matrix.append(nums)
print(total_sum)
print(matrix)
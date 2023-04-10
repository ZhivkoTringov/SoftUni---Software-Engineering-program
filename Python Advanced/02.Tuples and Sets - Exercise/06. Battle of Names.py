n = int(input())

odd_set = set()
even_set = set()

even_sum = 0
odd_sum = 0

for i in range(1, n+1):
    name = sum([ord(x) for x in input()]) // i
    if name % 2 == 0:
        even_set.add(name)
        even_sum += name
    else:
        odd_set.add(name)
        odd_sum += name

if even_sum == odd_sum:
    result = odd_set.union(even_set)
elif even_sum > odd_sum:
    result = odd_set.symmetric_difference(even_set)
else:
    result = odd_set.difference(even_set)

print(*result, sep=', ')
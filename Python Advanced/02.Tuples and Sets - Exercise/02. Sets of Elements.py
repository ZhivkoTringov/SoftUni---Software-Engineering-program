n, m = [int(x) for x in input().split()]
first_set = set()
second_set = set()
subset = set()
for _ in range(n):
    nums = int(input())
    first_set.add(nums)
for _ in range(m):
    nums = int(input())
    second_set.add(nums)
subset = first_set.intersection(second_set)
for i in subset:
    print(i)
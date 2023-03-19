nums = list(map(int, input().strip()))
nums.sort(reverse= True)
print(*nums, sep='')
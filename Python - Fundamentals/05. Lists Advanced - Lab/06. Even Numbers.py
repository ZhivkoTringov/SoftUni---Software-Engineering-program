nums = list(map(int, input().split(', ')))
result = [i for i in range(len(nums)) if nums[i] % 2 == 0]
print(result)
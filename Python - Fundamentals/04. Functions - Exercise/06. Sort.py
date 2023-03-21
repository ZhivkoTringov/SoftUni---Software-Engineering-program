def sorted_nums(nums):
    nums = sorted(nums)
    return nums


numbs = list(map(int, input().split(' ')))
print(sorted_nums(numbs))
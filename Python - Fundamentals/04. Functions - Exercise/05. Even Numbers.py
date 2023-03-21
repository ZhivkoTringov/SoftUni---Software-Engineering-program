def even_numbers(nums):
    even=[]
    for even_nums in nums:
        if even_nums % 2 == 0:
            even.append(even_nums)
    return even


numbs = list(map(int, input().split(' ')))
print(even_numbers(numbs))

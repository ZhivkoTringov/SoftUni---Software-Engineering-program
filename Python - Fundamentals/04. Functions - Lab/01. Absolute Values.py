def absolute_values(nums):
    result = [abs(i) for i in nums]
    return result


numbers = list(map(float, input().split(' ')))
print(absolute_values(numbers))
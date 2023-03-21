def min_nums(numbers):
    min_num = min(numbers)
    return min_num


def max_nums(numbers):
    max_num = max(numbers)
    return max_num


def sum_num(numbers):
    sum_nums = sum(numbers)
    return sum_nums


numbs = list(map(int, input().split(' ')))
print(f'The minimum number is {min_nums(numbs)}')
print(f'The maximum number is {max_nums(numbs)}')
print(f'The sum number is: {sum_num(numbs)}')
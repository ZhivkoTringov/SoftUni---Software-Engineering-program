def rows_rhombus(nums, i):
    for space in range(nums - i):
        print(' ', end='')
    for star in range(1, i):
        print('*', end=' ')
    print('*')


def upper_funcs(nums):
    for i in range(1, nums + 1):
        rows_rhombus(nums, i)


def down_funcs(nums):
    for i in range(nums - 1, 0, -1):
        rows_rhombus(nums, i)


def print_rhombus(nums):
    upper_funcs(nums)
    down_funcs(nums)


nums = int(input())
print_rhombus(nums)
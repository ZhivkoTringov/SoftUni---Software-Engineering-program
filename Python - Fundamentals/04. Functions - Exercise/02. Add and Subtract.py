def add_func(a: int, b: int, c: int):
    result = a + b
    total = result - c
    return total


first_num = int(input())
second_num = int(input())
third_num = int(input())
print(add_func(first_num, second_num, third_num))
def min_num(num: int):
    new = [num]
    return min(new)


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(min_num(min(first_number, second_number, third_number)))

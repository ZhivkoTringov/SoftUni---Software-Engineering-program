from collections import deque

els = input().split()
nums = deque()

for el in els:
    if el in '+-*/':
        while len(nums) > 1:
            first = nums.popleft()
            second = nums.popleft()
            result = 0

            if el == '+':
                result = first + second
            elif el == '-':
                result = first - second
            elif el == '*':
                result = first * second
            else:
                result = first // second

            nums.appendleft(result)
    else:
        nums.append(int(el))
print(nums.popleft())
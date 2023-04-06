N = int(input())
stack = []
for _ in range(N):
    nums = input().split()
    command = nums[0]
    if command == '1':
        the_nums = int(nums[1])
        stack.append(the_nums)
    elif command == '2':
        if stack:
            stack.pop()
    elif command == '3':
        if stack:
            print(max(stack))
    elif command == '4':
        if stack:
            print(min(stack))
while stack:
    el = stack.pop()
    if stack:
        print(el, end= ', ')
    else:
        print(el)
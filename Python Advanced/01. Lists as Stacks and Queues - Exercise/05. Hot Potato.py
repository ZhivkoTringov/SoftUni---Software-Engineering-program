from collections import deque


kids = deque(input().split())
num = int(input())
while len(kids) > 1:
    kids.rotate(-num)
    print(f'Removed {kids.pop()}')
print(f'Last is {kids.popleft()}')
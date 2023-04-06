from collections import deque

quantity_of_food = int(input())
orders = deque(map(int, input().split()))
print(max(orders))
while orders:
    order = orders[0]
    if order > quantity_of_food:
        break
    else:
        quantity_of_food -= order
    order = orders.popleft()
if orders:
    print(f'Orders left: {" ".join([str(x) for x in orders])}')
else:
    print(f'Orders complete')
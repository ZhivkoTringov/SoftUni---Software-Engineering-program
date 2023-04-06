clothes = [int(x) for x in input().split()]
capacity = int(input())
racks = 1
current_capacity = capacity
while clothes:
    element = clothes[-1]
    if element > current_capacity:
        racks += 1
        current_capacity = capacity
    else:
        element = clothes.pop()
        current_capacity -= element
print(racks)
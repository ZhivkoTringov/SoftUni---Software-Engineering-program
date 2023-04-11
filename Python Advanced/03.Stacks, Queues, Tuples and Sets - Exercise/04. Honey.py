from collections import deque

bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
operators = deque(input().split())
honey = 0
while bees and nectar:
    current_bee = bees[0]
    current_nectar = nectar.pop()
    if current_nectar < current_bee:
        continue
    bees.popleft()
    current_operation = operators.popleft()
    if current_operation == '+':
        honey += abs(current_bee + current_nectar)
    elif current_operation == '-':
        honey += abs(current_bee - current_nectar)
    elif current_operation == '*':
        honey += abs(current_bee * current_nectar)
    elif current_operation == '/' and current_nectar > 0:
        honey += abs(current_bee / current_nectar)
print(f'Total honey made: {honey}')
if bees:
    print(f'Bees left: {", ".join(str(x) for x in bees)}')
if nectar:
    print(f'Nectar left: {", ".join(str(x) for x in nectar)}')
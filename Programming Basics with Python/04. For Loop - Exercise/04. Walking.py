total_steps = 0
while total_steps < 10000:
    steps = input()
    if steps == 'Going home':
        additional_steps = int(input())
        total_steps += additional_steps
        break
    total_steps += int(steps)
diff = abs(10000 - total_steps)
if total_steps >= 10000:
    print("Goal reached! Good job!")
    print(f'{diff} steps over the goal!')
else:
    print(f'{diff} more steps to reach goal.')
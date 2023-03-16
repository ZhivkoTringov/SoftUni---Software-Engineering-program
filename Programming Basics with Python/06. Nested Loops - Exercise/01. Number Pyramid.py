n = int(input())
current_value = 1
condition = False
for row in range(1, n + 1 ):
    for coll in range(row):
        print(f"{current_value}", end=' ')
        current_value += 1
        if current_value > n:
            condition = True
            break
    print()
    if condition:
        break

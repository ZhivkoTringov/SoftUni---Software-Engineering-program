destination = input()
total = 0
while destination != 'End':
    needed_money = float(input())
    total = 0
    while total < needed_money:
        saved_money = float(input())
        total += saved_money
    print(f'Going to {destination}!')
    destination = input()
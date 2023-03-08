budget = float(input())
season = input()
cost = 0
if budget <= 100:
    print('Somewhere in Bulgaria')
    if season == 'summer':
        cost = budget * 0.3
        print(f'Camp - {cost:.2f}')
    elif season == 'winter':
        cost = budget * 0.7
        print(f'Hotel - {cost:.2f}')
elif 100 < budget <= 1000:
    print('Somewhere in Balkans')
    if season == 'summer':
        cost = budget * 0.4
        print(f'Camp - {cost:.2f}')
    elif season == 'winter':
        cost = budget * 0.8
        print(f'Hotel - {cost:.2f}')
elif budget > 1000:
    print('Somewhere in Europe')
    if season == 'summer'or 'winter':
        cost = budget * 0.9
        print(f'Hotel - {cost:.2f}')
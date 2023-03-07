city = input()
sales = float(input())
bonus = 0
condition = True
if city == 'Sofia':
    if 0<= sales <= 500:
        bonus = sales * 0.05
    elif 500 < sales <= 1000:
        bonus = sales * 0.07
    elif 1000 < sales <= 10000:
        bonus = sales * 0.08
    elif 10000 < sales:
        bonus = sales * 0.12
    else:
        print('error')
        condition = False
elif city == 'Varna':
    if 0<= sales <= 500:
        bonus = sales * 0.045
    elif 500 < sales <= 1000:
        bonus = sales * 0.075
    elif 1000 < sales <= 10000:
        bonus = sales * 0.10
    elif 10000 < sales:
        bonus = sales * 0.13
    else:
        print('error')
        condition = False
elif city == 'Plovdiv':
    if 0<= sales <= 500:
        bonus = sales * 0.055
    elif 500 < sales <= 1000:
        bonus = sales * 0.08
    elif 1000 < sales <= 10000:
        bonus = sales * 0.12
    elif 10000 < sales:
        bonus = sales * 0.145
    else:
        print('error')
        condition =False
else:
    print('error')
    condition = False
if condition:
    print(f'{bonus:.2f}')
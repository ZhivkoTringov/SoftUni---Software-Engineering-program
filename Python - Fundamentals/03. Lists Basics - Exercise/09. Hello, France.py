from math import ceil

items_price = input().split('|')
budget = float(input())
old_price_list = []
new_price_list = []
sell_price = []
profit = 0
total_sell = 0
TOTAL = budget
for i in range(len(items_price)):
    each_item_and_price = items_price[i]
    items_separated = each_item_and_price.split('->')
    item = items_separated[0]
    old_price = float(items_separated[1])
    if item == 'Clothes' and old_price <= 50.00:
        old_price_list.append(old_price)
    elif item == 'Shoes' and old_price <= 35.00:
        old_price_list.append(old_price)
    elif item == 'Accessories' and old_price <= 20.50:
        old_price_list.append(old_price)
for j in old_price_list:
    if budget >= j:
        budget -= j
        new_price_list.append(j)
for k in new_price_list:
    new_price = k * 0.4 + k
    sell_price.append(new_price)
for l in sell_price:
    print(f"{l:.2f}", end=' ')
for m in sell_price:
    total_sell += m
profit = total_sell - TOTAL + budget
print()
print(f'Profit: {profit:.2f}')
if total_sell + budget >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')
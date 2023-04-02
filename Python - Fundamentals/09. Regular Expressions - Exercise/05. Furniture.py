import re
pattern = r'>>([A-Za-z]+)<<(\d+\.?\d+)!(\d*)'
total = 0
bought_furniture = []
command = input()
while command != 'Purchase':
    match = re.search(pattern, command)
    if match:
        furniture, price, quantity = match.groups()
        bought_furniture.append(furniture)
        total += int(quantity) * float(price)
    command = input()
print('Bought furniture:')
for i in bought_furniture:
    print(i)
print(f'Total money spend: {total:.2f}')
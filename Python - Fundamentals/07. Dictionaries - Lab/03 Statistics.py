products = {}
command = input()
counter = 0
while command != 'statistics':
    product = command.split(': ')
    if product[0] not in products:
        products[product[0]] = int(product[1])
        counter += 1
    elif product[0] in products:
        products[product[0]] += int(product[1])
    command = input()
print('Products in stock:')
for j in products:
    print(f'- {j}: {products[j]}')
print(f'Total Products: {counter}')
total = sum(products.values())
print(f'Total Quantity: {total}')
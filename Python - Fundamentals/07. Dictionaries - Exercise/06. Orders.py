order = {}
command = input()
while command != 'buy':
    data = command.split(' ')
    name = data[0]
    price = float(data[1])
    quantity = int(data[2])
    if name not in order:
        order[name] = []
        order[name].append(price)
        order[name].append(quantity)
    elif name in order and order[name][0] == price:
        order[name][1] += quantity
    elif name in order and order[name][0] != price:
        order[name].pop(0)
        order[name].insert(0, price)
        order[name][1] += quantity
    command = input()
for key, value in order.items():
    print(f'{key} -> {(value[0] * value[1]):.2f}')
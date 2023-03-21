def calculate_total_price(order: str, price: int):
    total = 0
    if order == 'coffee':
        total += 1.5 * price
    elif order == 'water':
        total += 1 * price
    elif order == 'coke':
        total += 1.4 * price
    elif order == 'snacks':
        total += 2 * price
    return f'{total:.2f}'


name = input()
num_orders = int(input())
print(calculate_total_price(name, num_orders))

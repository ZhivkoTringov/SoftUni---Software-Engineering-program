budget = int(input())
counter = 0
while True:
    product_prices = input()
    if product_prices == 'End':
        print('You bought everything needed.')
        break
    counter += int(product_prices)
    if budget < counter:
        print('You went in overdraft!')
        break
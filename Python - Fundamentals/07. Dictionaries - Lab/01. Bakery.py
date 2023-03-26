food_and_quantities = input().split(' ')
products = {}
for i in range(0, len(food_and_quantities), 2):
    products[food_and_quantities[i]] = int(food_and_quantities[i + 1])
print(products)
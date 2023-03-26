products_and_quantities = input().split(' ')
products = {}
for i in range(0, len(products_and_quantities), 2):
    products[products_and_quantities[i]] = int(products_and_quantities[i + 1])
searched_products = input().split(' ')
for i in searched_products:
    if i in products.keys():
        print(f"We have {products[i]} of {i} left")
    else:
        print(f"Sorry, we don't have {i}")
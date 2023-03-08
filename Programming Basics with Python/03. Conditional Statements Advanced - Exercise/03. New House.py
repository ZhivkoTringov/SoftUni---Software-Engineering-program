type_of_flowers = input()
num_flowers = int(input())
budget = int(input())
price = 0
if type_of_flowers == 'Roses':
    if num_flowers > 80:
        price = 5 - (5 * 0.1)
    elif num_flowers <=80:
        price = 5
elif type_of_flowers == 'Dahlias':
    if num_flowers > 90:
        price = 3.80 - (3.80 * 0.15)
    elif num_flowers <= 90:
        price = 3.80
elif type_of_flowers == 'Tulips':
    if num_flowers > 80:
        price = 2.80 - (2.80 * 0.15)
    elif num_flowers <= 80:
        price = 2.80
elif type_of_flowers == 'Narcissus':
    if num_flowers < 120:
        price = 3.00 + (3.00 * 0.15)
    elif num_flowers >= 120:
        price = 3.00
elif type_of_flowers == 'Gladiolus':
    if num_flowers < 80:
        price = 2.50 + (2.50 * 0.20)
    elif num_flowers >= 80:
        price = 2.50
sum = price * num_flowers
diff = abs(budget - sum)
if budget >= sum:
    print(f'Hey, you have a great garden with {num_flowers} {type_of_flowers} and {diff:.2f} leva left.')
elif budget < sum:
    print(f'Not enough money, you need {diff:.2f} leva more.')
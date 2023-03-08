budget = int(input())
season = input()
num_fishers = int(input())
boat_price = 0
if season == 'Spring':
    boat_price = 3000
elif season == 'Summer' or season == 'Autumn':
    boat_price = 4200
elif season == 'Winter':
    boat_price = 2600

if num_fishers <= 6:
    boat_price -= boat_price * 0.1
elif 6 < num_fishers <= 11:
    boat_price -= boat_price * 0.15
elif num_fishers > 11:
    boat_price -= boat_price * 0.25

if num_fishers % 2 ==0 and season !='Autumn':
    boat_price -= boat_price * 0.05
diff = abs(budget - boat_price)
if budget >= boat_price:
    print(f'Yes! You have {diff:.2f} leva left.')
elif budget < boat_price:
    print(f'Not enough money! You need {diff:.2f} leva.')
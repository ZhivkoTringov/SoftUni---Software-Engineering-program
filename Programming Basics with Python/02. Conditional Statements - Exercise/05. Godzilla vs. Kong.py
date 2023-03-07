budget = float(input())
num_of_extras = int(input())
price_for_dress_for_one_extra = float(input())
decor_price = budget * 0.1
extras_dress_price = num_of_extras * price_for_dress_for_one_extra
if num_of_extras > 150:
    extras_dress_price -= extras_dress_price * 0.1
total_sum_needed = decor_price + extras_dress_price
diff = abs(budget - total_sum_needed)
if budget >= total_sum_needed:
    print('Action!')
    print(f'Wingard starts filming with {diff:.2f} leva left.')
elif budget < total_sum_needed:
    print('Not enough money!')
    print(f'Wingard needs {diff:.2f} leva more.')

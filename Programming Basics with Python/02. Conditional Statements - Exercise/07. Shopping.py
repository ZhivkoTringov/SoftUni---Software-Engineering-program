budget = float(input())
n = int(input())
m = int(input())
p = int(input())
n_price_per_one = 250
total_n = n * n_price_per_one
m_price_per_one = total_n * 0.35
total_m = m_price_per_one * m
p_price_per_one = total_n * 0.1
total_p = p_price_per_one * p
order = total_n + total_m + total_p
if n > m:
    order -= order * 0.15
diff = abs(budget - order)
if budget >= order:
    print(f'You have {diff:.2f} leva left!')
else:
    print(f'Not enough money! You need {diff:.2f} leva more!')
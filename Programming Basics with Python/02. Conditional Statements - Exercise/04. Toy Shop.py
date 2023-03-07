vacation = float(input())
num_puzzles = int(input())
num_talking_dolls = int(input())
num_bears = int(input())
num_minions = int(input())
num_trucks = int(input())
order = num_puzzles * 2.6 + num_talking_dolls * 3 \
        + num_bears * 4.1 + num_minions * 8.2 \
        + num_trucks * 2
toys = num_puzzles + num_talking_dolls + num_bears + num_minions + num_trucks
if toys >= 50:
    order -= order * 0.25
rent = order * 0.1
profit = order - rent
diff = abs(profit - vacation)
if profit >= vacation:
    print(f'Yes! {diff:.2f} lv left.')
else:
    print(f'Not enough money! {diff:.2f} lv needed.')
from math import floor

companions = int(input())
days = int(input())
coins = 0
day_counter = 0
coins_per_companion = 0
for i in range(days):
    day_counter += 1
    if day_counter % 10 == 0:
        companions -= 2
    if day_counter % 15 == 0:
        companions += 5
    if day_counter % 3 == 0:
        coins -= 3 * companions
    if day_counter % 5 == 0:
        coins += 20 * companions
        if day_counter % 3 == 0:
            coins -= 2 * companions
    coins += 50
    coins -= 2 * companions
    if companions <= 0:
        coin_per_companion = 0
    else:
        coins_per_companion = floor(coins / companions)
print(f'{companions} companions received {coins_per_companion} coins each.')
bonus_points = int(input())
bonus = 0
if bonus_points <= 100:
    bonus = 5
elif 100 < bonus_points <= 1000:
    bonus = bonus_points * 0.2
elif bonus_points > 1000:
    bonus = bonus_points * 0.1
if bonus_points % 2 == 0:
    bonus = bonus + 1
elif bonus_points % 10 == 5:
    bonus = bonus + 2
print(bonus)
print(bonus + bonus_points)
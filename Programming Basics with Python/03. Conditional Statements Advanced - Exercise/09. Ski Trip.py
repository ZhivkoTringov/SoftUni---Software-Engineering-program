days = int(input())
type_of_occupation = input()
statement = input()
cost = 0
nights = days - 1
if type_of_occupation == 'room for one person':
    cost = 18 * nights
elif type_of_occupation == 'apartment':
    cost = 25 * nights
    if nights < 10:
        cost -= cost * 0.3
    elif 10 <= nights <= 15:
        cost -= cost * 0.35
    elif nights > 15:
        cost -= cost * 0.50
elif type_of_occupation == 'president apartment':
    cost = 35 * nights
    if nights < 10:
        cost -= cost * 0.1
    elif 10 <= nights <= 15:
        cost -= cost * 0.15
    elif nights > 15:
        cost -= cost * 0.20
if statement == 'positive':
    cost += cost *0.25
elif statement == 'negative':
    cost -= cost * 0.10
print(f'{cost:.2f}')
change = int(float(input()) * 100)
counter = 0
while change > 0:
    if change >= 200:
        change -= 200
        counter += 1
    if 200 >change >= 100:
        change -= 100
        counter += 1
    if 100 > change >= 50:
        change -= 50
        counter += 1
    if 50 > change >= 20:
        change -= 20
        counter += 1
    if 20 > change >= 10:
        change -= 10
        counter += 1
    if 10 > change >= 5:
        change -= 5
        counter += 1
    if 5 > change >= 2:
        change -= 2
        counter += 1
    if 2 > change >= 1:
        change -= 1
        counter += 1
print(counter)
symbols = input().split('|')
matrix = []

while symbols:
    symbol = symbols.pop().split()
    for el in symbol:
        matrix.append(el)
print(*matrix, sep=' ')
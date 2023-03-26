chars = ''.join(x for x in input().split())
symbols = {}
for i in chars:
    if i not in symbols.keys():
        symbols[i] = 0
    symbols[i] += 1
for key, value in symbols.items():
    print(f'{key} -> {value}')
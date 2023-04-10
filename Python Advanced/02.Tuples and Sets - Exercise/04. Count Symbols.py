txt = input()
symbols = {}

for i in txt:
    if i not in symbols:
        symbols[i] = []
    symbols[i].append(1)
for key, value in sorted(symbols.items()):
    print(f'{key}: {len(value)} time/s')
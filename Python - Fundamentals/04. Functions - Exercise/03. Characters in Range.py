def charts(a, b):
    a = ord(first_symbol)
    o = ord(second_symbol)
    new = []
    for symbol in range(a + 1, o):
        new.append(chr(symbol))
    return new


first_symbol = input()
second_symbol = input()
print(' '.join(charts(first_symbol, second_symbol)))

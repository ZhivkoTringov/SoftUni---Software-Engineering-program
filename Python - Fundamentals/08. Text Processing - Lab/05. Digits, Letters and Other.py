def find_letters(symbol: str):
    return ''.join([str(ch) for ch in symbol if ch.isalpha()])


def find_digits(symbol):
    return ''.join([ch for ch in symbol if ch.isdigit()])


def find_others(symbol):
    return ''.join([ch for ch in symbol if not ch.isalpha() and not ch.isdigit()])


symbols = input()
print(find_digits(symbols))
print(find_letters(symbols))
print(find_others(symbols))

def sorting_cheeses(**kwargs):
    sorted_cheeses = sorted(kwargs.items(), key=lambda kvpt: (-len(kvpt[1]), kvpt[0]))
    result = ''

    for name, quantity in sorted_cheeses:
        result += name + "\n"
        sorted_quantity = sorted(quantity, reverse=True)
        result += "\n".join(str(x) for x in sorted_quantity) + "\n"
    return result

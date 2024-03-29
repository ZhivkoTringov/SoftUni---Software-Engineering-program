def even_odd_filter(**kwargs):
    numbers = {}

    for key, value in kwargs.items():
        if key == 'even':
            numbers[key] = [x for x in value if x % 2 == 0]
        else:
            numbers[key] = [x for x in value if x % 2 != 0]
    return dict(sorted(numbers.items(), key=lambda x: -len(x[1])))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))

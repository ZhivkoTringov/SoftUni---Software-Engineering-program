def read_next(*args):
    for iterable in args:
        for x in iterable:
            yield x


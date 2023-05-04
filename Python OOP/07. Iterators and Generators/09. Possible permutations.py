from itertools import permutations


def possible_permutations(seq):
    for el in permutations(seq):
        yield list(el)

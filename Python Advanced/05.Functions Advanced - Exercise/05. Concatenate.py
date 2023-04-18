def concatenate(*args, **kwargs):
    word = ''.join(args)

    for key, val in kwargs.items():
        if key in word:
            word = word.replace(key, val)
    return word

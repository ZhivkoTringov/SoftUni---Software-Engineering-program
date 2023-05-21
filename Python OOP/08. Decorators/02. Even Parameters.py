def even_parameters(func_ref):
    def wrapper(*args):
        for el in args:
            if not isinstance(el, int) or el % 2 != 0:
                return 'Please use only even numbers!'
        return func_ref(*args)
    return wrapper

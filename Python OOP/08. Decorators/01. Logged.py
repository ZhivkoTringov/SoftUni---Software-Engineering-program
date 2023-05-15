def logged(func_ref):
    def wrapper(*args):
        func_name = func_ref.__name__
        func_result = func_ref(*args)

        return f'you called {func_name}{args}\nit returned {func_result}'
    return wrapper
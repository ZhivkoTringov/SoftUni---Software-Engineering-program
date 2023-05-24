def cache(func_ref):
    log = {}

    def wrapper(num):
        if num in log:
            return log[num]
        result = func_ref(num)
        log[num] = result

        return result

    wrapper.log = log
    return wrapper

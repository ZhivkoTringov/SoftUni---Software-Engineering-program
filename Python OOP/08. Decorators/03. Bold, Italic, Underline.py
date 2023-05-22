def format_text(tag, text):
    return f'<{tag}>{text}</{tag}>'


def make_underline(func_ref):
    def wrapper(*args):
        func_result = func_ref(*args)
        return format_text('u', func_result)
    return wrapper


def make_italic(func_ref):
    def wrapper(*args):
        func_result = func_ref(*args)
        return format_text('i', func_result)
    return wrapper


def make_bold(func_ref):
    def wrapper(*args):
        func_result = func_ref(*args)
        return format_text('b', func_result)
    return wrapper
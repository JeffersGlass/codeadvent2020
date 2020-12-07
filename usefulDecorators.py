import functools

def sayFunction(func):

    @functools.wraps(func)
    def wrapper_say(*args, **kwargs):
        print(f"Function {func.__name__!r} was called with arguments {args} and {kwargs}")
        value = func(*args, **kwargs)
        print(f"Return value from calling with {args} was {value}")
        return value
    return wrapper_say
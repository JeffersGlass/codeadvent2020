import time
import functools

def timer(func):
    """Print the runtime of the decorated functions

    Args:
        func ([function]): [Will be the function to be decorated - this function should only be used as a decorator]
    """
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        elapsed = time.perf_counter() - start_time
        print(f"Function {func.__name__!r} took {elapsed:.4f} seconds to complete.")
        return value
    return wrapper_timer
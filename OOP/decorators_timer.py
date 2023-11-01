from datetime import datetime
import functools

""" decorator """


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        started = datetime.now()
        print(f'{func.__name__} started at {started}')
        function_result = func(*args, **kwargs)
        ended = datetime.now()
        duration = ended - started
        print(f'{func.__name__} ended at {ended}')
        print(f'{func.__name__} duration {duration}')
        return function_result

    return wrapper


@timer
def add_5(number: int) -> int:
    result = number + 5
    return result


result = add_5(4)
print(result)

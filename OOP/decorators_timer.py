from datetime import datetime
import functools
import logging
""" decorators """

def function_log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            function_result = func(*args, **kwargs)
            return function_result
        except Exception as e:
            print(e)

    return wrapper


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


@function_log
def add_5(number: int) -> int:
    result = number + 5
    return result

@function_log
@timer
def divide(numerator: int, denominator: int) -> float:
    result = numerator / denominator
    return result


result = divide(numerator=8, denominator=2)
print(result)

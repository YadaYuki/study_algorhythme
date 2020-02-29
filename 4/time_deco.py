import time
from functools import wraps


def timeit(func_name,ndigits):
    """
    message:message print with time
    ndigits: the num of digits of time
    """
    def outer_wrapper(func):
        @wraps(func)
        def inner_wrapper(*args,**kwargs):
            start = time.time()
            result = func(*args,**kwargs)
            end = time.time()
            print("{func_name} is excecuting:{sec}".format(func_name=func_name,sec = round(end-start,ndigits)))
            return result
        return inner_wrapper
    return outer_wrapper
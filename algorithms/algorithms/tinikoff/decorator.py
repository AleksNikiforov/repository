from datetime import datetime

def decorator_for_my_func(my_func):
    def inner_func(*args, **kwargs):
        time_start = datetime.now()
        my_func(*args, **kwargs)
        time_stop = datetime.now()
        timing = time_stop - time_start
        print(timing)
    return inner_func


@decorator_for_my_func
def summ(a, b):
    return a + b


summ(1, 2)

import time

def calculate_time(func):
    def wrapper(*args, **kwargs):
        t0 = time.time()
        ret = func(*args, **kwargs)
        t1 = time.time()
        print(f'Total time {t1 - t0}')
        return ret
    return wrapper


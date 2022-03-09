
def doubler(func):
    def wrapper(*args, **kwargs):
        r0 = func(*args, **kwargs)
        r1 = func(*args, **kwargs)
        return (r0, r1)
    return wrapper


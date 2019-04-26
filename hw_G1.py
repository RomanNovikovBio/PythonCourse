def decorator(func):
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        f = open(f'{func.__name__}.txt', 'w')
        f.write(str(result))
        f.close()
        return result
    return wrapped

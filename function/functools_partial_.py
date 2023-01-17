import functools

def multiply(x, y):
    return x * y

# partial(func, *arg, **kwargs)
double = functools.partial(multiply,2)

print(double(3))
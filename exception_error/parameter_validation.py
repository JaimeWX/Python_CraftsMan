def print_string(s):
    if not isinstance(s, str):
        raise TypeError('s must be string')
    print(s)

print_string(3)
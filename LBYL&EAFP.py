def incr_by_one_LBYL(value):
    """对输入整数加1，返回新的值

    :param value: 整型，或者可以转成整型的字符串
    :return: 整型结果
    """
    if isinstance(value, int):
        return value + 1
    elif isinstance(value, str) and value.isdigit():
        return int(value) + 1
    else:
        print(f'Unable to perform incr for value: "{value}"')

def incr_by_one_EAFP(value):
    """对输入整数加1，返回新的值

    :param value: 整型，或者可以转成整型的字符串
    :return: 整型结果
    """
    try:
        return int(value) + 1
    except (TypeError, ValueError) as e:
        print(f'Unable to perform incr for value: "{value}", error: {e}')

print(incr_by_one_EAFP(23))
print(incr_by_one_EAFP('23'))
print(incr_by_one_EAFP([]))
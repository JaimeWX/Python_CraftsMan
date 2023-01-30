import random

def provide_number(min_num, max_num):
    """
    装饰器：随机生成一个在 [min_num, max_num] 范围内的整数，
    并将其追加为函数的第一个位置参数
    """

    def wrapper(func):
        def decorated(*args, **kwargs):
            num = random.randint(min_num, max_num)
            # 将 num 追加为第一个参数，然后调用函数
            return func(num, *args, **kwargs)

        return decorated

    return wrapper

@provide_number(1, 100)
def print_random_number(num):
    print(num)

print_random_number()
import time
import random
'''
timer 装饰器接收待装饰函数 func 作为唯一的位置参数，并在函数内定义了一个新函数：decorated。

这些包装函数通常接收任意数目的可变参数 (*args, **kwargs)，主要通过调用原始函数 func 来完成工作。
在包装函数内部，常会增加一些额外步骤，比如打印信息、修改参数等。

当其他函数应用了 timer 装饰器后，包装函数 decorated 会作为装饰器的返回值，完全替换被装饰的原始函数 func。
'''
def timer(func):
    """装饰器：打印函数耗时"""

    def decorated(*args, **kwargs):
        st = time.perf_counter()
        ret = func(*args, **kwargs)
        print('time cost: {} seconds'.format(time.perf_counter() - st))
        return ret

    return decorated

@timer
def random_sleep():
    """随机睡眠一小会儿"""
    time.sleep(random.random())

random_sleep()
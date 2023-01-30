import wrapt
import random

def provide_number(min_num, max_num):
    @wrapt.decorator
    def wrapper(wrapped, instance, args, kwargs):
        # 参数含义：
        #
        # - wrapped：被装饰的函数或类方法
        # - instance：
        # - 如果被装饰者为普通类方法，则该值为类实例
        # - 如果被装饰者为 classmethod 类方法，则该值为类
        # - 如果被装饰者为类/函数/静态方法，则该值为 None
        #
        # - args：调用时的位置参数（注意没有 * 符号）
        # - kwargs：调用时的关键字参数（注意没有 ** 符号）
        #
        num = random.randint(min_num, max_num)
        # 无须关注 wrapped 是类方法还是普通函数，直接在头部追加参数
        args = (num,) + args
        return wrapped(*args, **kwargs)

    return wrapper

'''
修饰函数方法
'''
# @provide_number(1, 100)
# def print_random_number(num):
#     print(num)

# print_random_number()

'''
修饰类方法
'''
class Foo:
    @provide_number(1, 100)
    def print_random_number(self,num):
        print(num)

Foo().print_random_number()

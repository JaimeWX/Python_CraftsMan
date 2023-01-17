'''
当我们以 iter(callable, sentinel) 的方式调用 iter() 函数时，会拿到一个特殊的迭代器对象。
用循环遍历这个迭代器，会不断返回调用 callable() 的结果，假如结果等于 sentinel，迭代过程中止。
'''

from functools import partial

def count_digits_v3(fname):
    count = 0
    block_size = 1024 * 8
    with open(fname) as fp:
        # 使用 functools.partial 构造一个新的无须参数的函数
        _read = partial(fp.read, block_size) 

        # 利用 iter() 构造一个不断调用 _read 的迭代器
        for chunk in iter(_read, ''):
            for s in chunk:
                if s.isdigit():
                    count += 1
    return count
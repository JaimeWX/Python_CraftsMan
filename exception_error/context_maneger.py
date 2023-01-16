import random

class DummyContext:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        # __enter__ 会在进入管理器时被调用，同时可以返回结果
        # 这个结果可以通过 as 关键字被调用方获取
        #
        # 此处返回一个增加了随机后缀的 name
        return f'{self.name}-{random.random()}'

    def __exit__(self, exc_type, exc_val, exc_tb):
        # __exit__ 会在退出管理器时被调用
        print('Exiting DummyContext')
        return False

with DummyContext('jaime') as name:
    print(f'Name:{name}')

class Foo:
    def __call__(self,name): # __call__ 魔法方法是用来实现可调用对象的关键方法
        print(f'Hello,{name}')

foo = Foo()
print(callable(foo))
foo('xx') # 调用类实例时，可以像调用普通函数一样提供额外参数
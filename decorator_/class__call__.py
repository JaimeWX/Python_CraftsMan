class Foo:
    def __call__(self,name):
        print(f'Hello,{name}')

foo = Foo()
print(callable(foo))
foo('xx')
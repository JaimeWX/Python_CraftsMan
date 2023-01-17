def append_value(value, items=[]):
    """向 items 列表中追加内容，并返回列表"""
    items.append(value)
    return items

print(append_value('foo'))
print(append_value.__defaults__)
'''
在第二次调用时，函数并没有返回正确结果 ['bar']，而是返回了 ['foo', 'bar']，
这意味着参数 items 的值不再是函数定义的空列表 []，而是变成了第一次执行后的结果 ['foo']
之所以出现这个问题，是因为 Python 函数的参数默认值只会在函数定义阶段被创建一次，之后不论再调用多少次，函数内拿到的默认值都是同一个对象。
'''
print(append_value('bar'))
print(append_value.__defaults__)

append_value.__defaults__[0].append('baz')
print(append_value.__defaults__)

# items=[] 应该改为 items=None

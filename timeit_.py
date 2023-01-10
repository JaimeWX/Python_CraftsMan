import timeit

# 定义一个长度为 100 的词汇列表
WORDS = ['Hello', 'string', 'performance', 'test'] * 25

def str_cat():
    """使用字符串拼接"""
    s = ''
    for word in WORDS:
        s += word
    return s


def str_join():
    """使用列表配合 join 产生字符串
    """
    l = []
    for word in WORDS:
        l.append(word)
    return ''.join(l)

# 默认执行 100 万次
cat_spent = timeit.timeit(setup='from __main__ import str_cat', stmt='str_cat()')
print("cat_spent:", cat_spent)

join_spent = timeit.timeit(setup='from __main__ import str_join', stmt='str_join()')
print("join_spent", join_spent)
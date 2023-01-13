def generate_even(max_number):
    """一个简单生成器，返回 0 到 max_number 之间的所有偶数"""
    for i in range(0, max_number):
        if i % 2 == 0:
            yield i

# for i in generate_even(10):
#     print(i)

i = generate_even(10)
print(next(i))
print(next(i))

list_ = list(generate_even(10))
print(list_)
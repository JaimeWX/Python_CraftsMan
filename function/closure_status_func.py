import re

def make_cyclic_mosaic():
    """
    将匹配到的模式替换为其他字符，使用闭包实现轮换字符效果
    """
    char_index = 0
    mosaic_chars = ['*', 'x']

    def _mosaic(matchobj):
        nonlocal char_index
        char = mosaic_chars[char_index]
        char_index = (char_index + 1) % len(mosaic_chars)

        length = len(matchobj.group())
        return char * length
    '''
    重复调用时使用新的闭包函数对象，计数器重新从 0 开始，没有结果不稳定问题
    '''
    print(char_index)
    return _mosaic
'''
此处是 make_cyclic_mosaic() 而不是 make_cyclic_mosaic，
因为 make_cyclic_mosaic() 函数的调用结果才是真正的替换函数
'''
print(re.sub(r'\d+', make_cyclic_mosaic(), '商店共 100 个苹果，小明以 12 元每斤的价格买走了8 个'))

print(re.sub(r'\d+', make_cyclic_mosaic(), '商店共 100 个苹果，小明以 12 元每斤的价格买走了8 个'))
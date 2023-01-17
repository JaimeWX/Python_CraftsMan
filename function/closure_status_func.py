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

    return _mosaic

print(re.sub(r'\d+', make_cyclic_mosaic(), '商店共 100 个苹果，小明以 12 元每斤的价格买走了8 个'))
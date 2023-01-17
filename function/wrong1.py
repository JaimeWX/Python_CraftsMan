import re

_mosaic_char_index = 0

def mosaic_string(s):
    """用 * 替换输入字符串里面所有的连续数字"""
    return re.sub(r'\d+', mosaic_global_var, s) 

def mosaic_matchobj(matchobj): 
    """将匹配到的模式替换为等长星号字符串"""
    length = len(matchobj.group())
    return '*' * length

def mosaic_global_var(matchobj):
    """
    将匹配到的模式替换为其他字符，使用全局变量实现轮换字符效果
    """
    global _mosaic_char_index 
    mosaic_chars = ['*', 'x']

    char = mosaic_chars[_mosaic_char_index]
    # 递增马赛克字符索引值
    _mosaic_char_index = (_mosaic_char_index + 1) % len(mosaic_chars)

    length = len(matchobj.group())
    return char * length

print(mosaic_string("商店共 100 个苹果，小明以 12 元每斤的价格买走了 8 个"))

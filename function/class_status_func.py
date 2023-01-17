import re

class CyclicMosaic:
    """使用会轮换的屏蔽字符，基于类实现"""

    _chars = ['*', 'x']

    def __init__(self):
        self._char_index = 0 

    def generate(self, matchobj):
        char = self._chars[self._char_index]
        self._char_index = (self._char_index + 1) % len(self._chars)
        length = len(matchobj.group())
        return char * length

print(re.sub(r'\d+', CyclicMosaic().generate, '商店共 100 个苹果，小明以 12 元每斤的价格买走了 8 个'))
from functools import partial
from collections import defaultdict

def read_file_digits(fp, block_size=1024 * 8):
    """生成器函数：分块读取文件内容，返回其中的数字字符"""
    _read = partial(fp.read, block_size)
    for chunk in iter(_read, ''):
        for s in chunk:
            if s.isdigit():
                yield s

def count_digits_v4(fname):
    count = 0
    with open(fname) as file:
        for _ in read_file_digits(file):
            count += 1
    return count

def count_even_groups(fname):
    """分别统计文件里每个偶数字符出现的次数"""
    counter = defaultdict(int)
    with open(fname) as file:
        for num in read_file_digits(file):
            if int(num) % 2 == 0:
                counter[int(num)] += 1
    return counter
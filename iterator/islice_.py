'''
islice(seq, start, end, step) 函数和数组切片操作（list[start:stop:step]）接收的参数几乎完全一致。
'''

from itertools import islice

def parse_titles_v2(filename):
    with open(filename, 'r') as fp:
        # 设置 step=2，跳过无意义的 --- 分隔符
        for line in islice(fp, 0, None, 2):
            yield line.strip()
        

fp = parse_titles_v2('islice_.txt')
for line in fp:
    print(line)
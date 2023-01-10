'''
str.partition(sep) 的功能是按照分隔符 sep 切分字符串，
返回一个包含三个成员的元组：(part_before, sep, part_after)，它们分别代表分隔符前的内容、分隔符以及分隔符后的内容。
'''

s = '/data_source/lwl/2023-01-09/'
print(s.partition('/')[-1])

# results: ('', '/', 'data_source/lwl/2023-01-09/')
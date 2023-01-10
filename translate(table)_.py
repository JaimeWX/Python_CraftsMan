'''
str.translate(table) 方法有时也非常有用。
它可以按规则一次性替换多个字符，使用它比调用多次 replace 方法更快也更简单：
'''

s = '/data_source/lwl/2023-01-09/'

table = s.maketrans('/','|')
print(s.translate(table))
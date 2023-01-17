'''
# 未使用takewhile
for user in users:
    # 当第一个不合格的用户出现后，不再进行后面的处理
    if not is_qualified(user):
        break

    # 进行处理……
'''

'''
# 使用takewhile
from itertools import takewhile

for user in takewhile(is_qualified, users):
    # 进行处理……
'''

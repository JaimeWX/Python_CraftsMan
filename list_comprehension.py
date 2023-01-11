def remove_odd_mul_100(numbers):
# 用一个表达式完成 4 件事情
#
# 1. 遍历旧列表：for n in numbers
# 2. 对成员进行条件过滤：if n % 2 == 0
# 3. 修改成员： n * 100
# 4. 组装新的结果列表
#
    results = [n * 100 for n in numbers if n % 2 == 0]
numbers = [1, 2, 3]
numbers = (i * 2 for i in numbers)

# 第一次 in 判断会触发生成器遍历，找到 4 后返回 True
print(4 in numbers)
# 做第二次 in 判断时，生成器已被部分遍历过，无法再找到 4，因此返回意料外的结果
print(4 in numbers)
import copy
nums = [1, 2, 30, 4]
nums_copy = list(nums)
nums[3] = 6
print(nums,nums_copy)


d = {'foo': 1}
d2 = dict(d.items())
d['foo'] = 8
print(d,d2)
import copy
nums = [1, 2, 30, 4]
nums_copy = nums.copy()
nums[2] = 1
print(nums,nums_copy)

d = {'foo': 1}
d2 = d.copy()
d['foo'] = 8
print(d,d2)
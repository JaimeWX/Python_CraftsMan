import copy
nums = [1, 2, 30, 4]
nums_copy = copy.copy(nums)
nums[2] = 1
print(nums,nums_copy)
from collections import OrderedDict

nums = [10, 2, 3, 21, 10, 3]

no_duplicate_list = (OrderedDict.fromkeys(nums).keys())
print(list(no_duplicate_list))
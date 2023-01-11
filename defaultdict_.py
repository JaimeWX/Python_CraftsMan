from collections import defaultdict

int_dict = defaultdict(int)
int_dict['foo'] += 1

print(int_dict)

dict_ = dict(int_dict)
print(dict_)
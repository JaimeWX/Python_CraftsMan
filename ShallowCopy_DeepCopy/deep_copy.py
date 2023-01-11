import copy

items = [1, ['foo', 'bar'], 2, 3]
items_copy = copy.deepcopy(items)

items[0] = 100
items[1].append('xxx')

print(items)
print(items_copy)

from collections import MutableMapping
from collections import defaultdict

class UpperDict(dict):
    """总是把 key 转为大写"""
    def __setitem__(self, key, value):
        super().__setitem__(key.upper(), value)

b = UpperDict()
b['foo'] = 1
print(b)

b.update({'bar':2})
print(b)

class PerfLevelDict(MutableMapping):
    def __init__(self):
        self.data = defaultdict(int)

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key,value):
        self.data[key.upper()] = value

    def __delitem__(self, key):
        del self.data[key]

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)


d = PerfLevelDict()
d['foo'] = 1
print(d)

d.update({'bar':2})
print(dict(d))

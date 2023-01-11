d = {'title': 'foobar'}
d.setdefault('items', []).append('foo')
print(d)
d.setdefault('items', []).append('bar')
print(d)

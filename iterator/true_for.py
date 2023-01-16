'''


for name in names:
    print(name)
'''

names = ['foo', 'bar', 'foobar']

iterator = iter(names)
while True:
    try:
        name = next(iterator)
        print(name)
    except StopIteration:
        break
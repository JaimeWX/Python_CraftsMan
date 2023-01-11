d = {'foo': 1}
d2 = {key:value for key,value in d.items()}
d['foo'] = 8
print(d,d2)
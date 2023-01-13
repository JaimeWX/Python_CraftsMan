d1 = {'name': 'apple'}
d2 = {'price': 10}

d_all1 = {*d1,*d2}
print(d_all1)

d_all2 = {**d1,**d2}
print(d_all2)

list_ = [1, 2, *range(3)]
print(list_)

l1 = [1,2]
l2 = [3,4]
l_all = [*l1,*l2]
print(l_all)


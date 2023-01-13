def incr_by_key(d, key):
    try:
        d[key] += 1
        print(d[key])
    except KeyError:
        print(f'key {key} does not exists, re-raise the exception')
        raise

dict_ = {'jaime':1}
dict1_ = {'jaime':'xx'}

print(incr_by_key(dict_,'jaime'))
print(incr_by_key(dict1_,'jaime'))
print(incr_by_key(dict1_,'wx'))
def fun(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)
fun("a", "b", "c", param1="a", param2="b", param3="c")
fun(*["a","b","c"], param1="a", param2="b", param3="c")

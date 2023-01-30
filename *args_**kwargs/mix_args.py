def fun(name, *args, age=None, **kwargs):
    print("name:", name)
    print("args:", args)
    print("age:", age)
    print("kwargs:", kwargs)

fun(1, 2, 3, a=1, b=2, c=3)
fun("helloworld", 1, 2, 3, age=12, a=1, b=2, c=3)

def func1(*args):
    # 打印参数类型
    print(type(args))
    # 打印参数
    print(args)
    
func1("a", "b", "c")
func1(["a", "b", "c"])
# 将一个列表变为元组，需要在传入参数的前面加上一个*
func1(*["a", "b", "c"])
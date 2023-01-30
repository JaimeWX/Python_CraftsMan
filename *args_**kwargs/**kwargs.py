def func2(**kwargs):
    # 转为字典
    print(type(kwargs))
    for key, value in kwargs.items():
        print("{} = {}".format(key,value))
    
func2(param1="a", param2="b", param3="c")
# 也可以直接传入一个字典
dicts={'param1':"a", 'param2':"b", 'param3':"c"}
func2(**dicts)

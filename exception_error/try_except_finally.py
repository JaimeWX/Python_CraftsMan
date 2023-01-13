def safe_int(value):
    """尝试把输入转换为整数"""
    try:
        return int(value)
    except TypeError:
        # 当某类异常被抛出时，将会执行对应 except 下的语句
        print(f'type error: {type(value)} is invalid')
    except ValueError:
        # 你可以在一个 try 语句块下写多个 except
        print(f'value error: {value} is invalid')
    finally:
        # finally 里的语句，无论如何都会被执行，哪怕已经执行了 return
        print('function completed')

print(safe_int(None))
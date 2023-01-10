from decimal import Decimal

def float_precision(num1:float,num2:float):
    '''练习如何使用Decimal
    :param num1: 加法运算的第一个数
    :param num2: 加法运算的第二个数
    '''
    return Decimal(str(num1))+Decimal(str(num2))

print(float_precision(0.1,0.2))

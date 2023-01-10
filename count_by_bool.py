from typing import List

def count_even_by_bool(numbers:List[int]):
    '''使用布尔值统计一个列表中有多少个偶数
    :param: ...
    
    '''
    count = sum(i%2==0 for i in numbers)
    return count

numbers = [1, 2, 4, 5, 7]
print(count_even_by_bool(numbers=numbers))
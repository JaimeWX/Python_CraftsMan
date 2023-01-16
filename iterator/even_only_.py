def even_only(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num


def sum_even_only_v2(numbers):
    """对 numbers 里面所有的偶数求和"""
    result = 0
    for num in even_only(numbers):
        result += num
    return result


nums = [x for x in range(1, 11)]
print(sum_even_only_v2(nums))

def all_numbers_gt_10(numbers):
    return bool(numbers) and all(n > 10 for n in numbers)

def any_numbers_gt_10(numbers):
    return bool(numbers) and any(n > 10 for n in numbers)

numbers = [1,23,10]
print(all_numbers_gt_10(numbers))
print(any_numbers_gt_10(numbers))
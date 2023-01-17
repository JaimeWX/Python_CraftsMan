import time
from functools import lru_cache

@lru_cache(maxsize=128)
def calculate_score(class_id):
    print(f'Calculating score for class: {class_id}...')
    time.sleep(5)
    return 42

class_id = 23
test_ = calculate_score(class_id)
print(test_)
test_again = calculate_score(class_id)
print(test_again)
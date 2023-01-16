class CreateItemError(Exception):
    """创建 Item 失败

    :param error_code: 错误代码
    :param message: 错误信息
    """

    def __init__(self, error_code, message):
        self.error_code = error_code
        self.message = message
        super().__init__(f'{self.error_code} - {self.message}')

# 抛出异常时指定 error_code
raise CreateItemError('name_too_long', 'name of item is too long')
raise CreateItemError('items_full', 'items is full')

def create_item(name):
    if len(name) > MAX_LENGTH_OF_NAME:
        raise CreateItemError('name of item is too long')
    if len(get_current_items()) > MAX_ITEMS_QUOTA:
        raise CreateErrorItemsFull('items is full')
    return Item(name=name)

def create_from_input():
    name = input()
    try:
        item = create_item(name)
    except CreateErrorItemsFull as e:
        clear_all_items()
        print(f'create item failed: {e}')
    except CreateItemError as e:
        print(f'create item failed: {e}')
    else:
        print(f'item<{name}> created')
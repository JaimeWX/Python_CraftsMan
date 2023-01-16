class CreateItemError(Exception):
    """创建 Item 失败"""


class CreateErrorItemsFull(CreateItemError):
    """当前的 Item 容器已满"""


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
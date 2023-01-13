class UserCollection:
    """用于保存多个用户的集合工具类"""

    def __init__(self, users):
        self.items = users

    def __len__(self):
        return len(self.items)
    
    def __bool__(self):
        return len(self.items) > 10

users = UserCollection(['piglei', 'raymond'])
print(len(users))
print(bool(users))
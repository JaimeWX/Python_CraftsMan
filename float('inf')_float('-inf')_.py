def sort_users_inf(users):

    def key_func(username):
        age = users[username]
        # 当年龄为空时，返回正无穷大作为 key，因此就会被排到最后
        return age if age is not None else float('inf')

    return sorted(users.keys(), key=key_func)

users = {"tom": 19, "jenny": 13, "jack": None, "andrew": 43}
print(sort_users_inf(users))

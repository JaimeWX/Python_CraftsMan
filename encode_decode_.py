# 字符串编码成为字节串
str_obj = 'Hello, 世界'
print(str_obj)
print(type(str_obj))
bin_str = str_obj.encode('UTF-8')
print(bin_str)
print(type(bin_str)
)

# 创建字节串
bin_obj = b'jaime'
print(bin_obj)
print(type(bin_obj))

# 字节串解码成为字符串
print(bin_obj.decode())
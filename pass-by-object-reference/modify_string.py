def add_str(in_func_obj):
    print(f'In add [before]: in_func_obj="{in_func_obj}"')
    in_func_obj += ' suffix'
    print(f'In add [after]: in_func_obj="{in_func_obj}"')


orig_obj = 'foo'
print(f'Outside [before]: orig_obj="{orig_obj}"')
add_str(orig_obj)
print(f'Outside [after]: orig_obj="{orig_obj}"')

# 函数外的 orig_obj 变量所指向的值没有受到任何影响
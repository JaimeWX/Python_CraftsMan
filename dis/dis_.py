'''
add() 函数的反汇编结果主要展示了下面几种操作。
    (1) 两次 LOAD_FAST：分别把局部变量 x 和 y 的值放入栈顶。
    (2) BINARY_ADD：从栈顶取出两个值（也就是 x 和 y 的值），执行加法操作，将结果放回栈顶。
    (3) RETURN_VALUE：返回栈顶的结果。
'''

import dis

def do_something(delta_seconds):
    if delta_seconds < 11 * 24 * 3600:
        return

print(dis.dis(do_something))
'''
以 yield 关键字为界
    yield 前的逻辑会在进入管理器时执行（类似于 __enter__）
    yield 后的逻辑会在退出管理器时执行（类似于 __exit__）
'''

from contextlib import contextmanager

@contextmanager
def create_conn_obj(host, port, timeout=None):
    """创建连接对象，并在退出上下文时自动关闭"""
    conn = create_conn(host, port, timeout=timeout)
    try: # 如果要在上下文管理器内处理异常，必须用 try 语句块包裹 yield 语句
        yield conn 
    finally: 
        conn.close()
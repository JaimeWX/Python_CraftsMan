class ignore_closed:
    """忽略已经关闭的连接"""

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type == AlreadyClosedError:
            return True
        return False

with ignore_closed():
    close_conn(conn)
import time
import functools

class DelayedStart:
    """在执行被装饰函数前，等待 1 秒钟"""

    def __init__(self, func,*,duration=1):
        functools.update_wrapper(self, func) 
        self.duration = duration
        self.func = func

    def __call__(self, *args, **kwargs): 
        print(f'Wait for {self.duration} second before starting...')
        time.sleep(self.duration)
        return self.func(*args, **kwargs)

    def eager_call(self, *args, **kwargs): 
        """跳过等待，立刻执行被装饰函数"""
        print('Call without delay')
        return self.func(*args, **kwargs)

def delayed_start(**kwargs):
    """装饰器：推迟某个函数的执行"""
    return functools.partial(DelayedStart, **kwargs)

@delayed_start(duration=2)
def hello():
    print('Hello World.')

hello()
hello.eager_call()
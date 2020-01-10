# 装饰器副作用

import time
from functools import wraps


def decorator(func):
    @wraps(func)
    def wrapper():
        print(time.time())
        func()

    return wrapper


@decorator
def f1():
    '''
    This is f1
    '''
    print(f1.__name__)


print(help(f1))
f1()

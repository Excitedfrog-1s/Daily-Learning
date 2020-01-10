import time


# 装饰器 实现AOP编程思想
# 可以适应不同的参数形式
# kw = key word
# 也体现了代码的复用
def decorator(func):
    def wrapper(*args, **kw):  #解决不同函数有不同参数问题
        print(time.time())
        func(*args, **kw)

    return wrapper


@decorator
def f1(func_name):
    print('This is a function' + func_name)


@decorator
def f2(func_name1, func_name2):
    print('This is a function' + func_name1)
    print('This is a function' + func_name2)


@decorator
def f3(func_name1, func_name2, **kw):
    print('This is a function' + func_name1)
    print('This is a function' + func_name2)
    print(kw)


f1('test func')
f2('test func1', 'test func2')
f3('test func1', 'test func2', a=1, b=2, c='123')
# 不需要改变调用方式为下面两行的形式
# f = decorator(f1)
# f()

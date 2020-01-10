# 装饰器
import time

# print(time.time())  Unix时间戳，或称POSIX时间
# 为每一个函数增加打印时间功能，遵循开闭原则，利用函数式编程特性
# 或者使用装饰器 (c7.py)


def f1():
    print('This is a function')


def f2():
    print('This is a function')


# 函数式编程解决方法：
def print_current_time(func):
    print(time.time())
    func()


print_current_time(f1)
print_current_time(f2)
# f1()

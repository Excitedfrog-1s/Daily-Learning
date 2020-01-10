# coding=utf-8
'''
# c = 50


def demo():
    c = 50
    for i in range(0, 9):
        c += 1
    print(c)


# print(c)
demo()
'''

# 链式 作用域链 作用域具有逐级寻找的过程
c = 1
'''
def func1():
    c = 2

    def func2():
        c = 3
        print(c)

    func2()


func1()
'''

# global关键字可让外部函数调用函数内变量


def demo():
    global c
    c = 2


demo()
print(c)

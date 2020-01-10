# coding=utf-8
# 函数

'''
print()
a = 1.1239
result = round(a, 3)
print(result)
1.功能性
2.隐藏细节
3.避免编写重复代码
'''

# 参数列表可以没有

# 实现两个数字的相加：
# 打印输入的参数


def add(x, y):
    result = x + y
    return result


def printf(code):
    print(code)
    return code


a = add(1, 2)
b = printf('Python')
print(a, b)

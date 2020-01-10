# coding=utf-8
'''
参数
1.必须参数 形参 实参
2.关键字参数
3.默认参数 需放在其他参数后面
4.可变参数 in c5.py
5.关键字可变参数 in c6.py
'''


def add(x, y):
    # 形式参数 形参
    result = x + y
    return result


# c = add(2, 3) 实参
c = add(y=3, x=2)
# 关键字参数
print(c)

# coding=utf-8
# 序列解包 链式赋值

a, b, c = 1, 2, 3
# a = b = c = 1
d = 1, 2, 3
print(type(d))
a, b, c = d
print d

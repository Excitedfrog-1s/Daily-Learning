# reduce 连续计算，连续调用lambda表达式
from functools import reduce
list_x = [1, 2, 3, 4, 5, 6, 7, 8]
r = reduce(lambda x, y: x + y, list_x, 10)
print(r)


# reduce加普通函数
def add(a, b):
    return a + b


s = reduce(add, list_x)
print(s)

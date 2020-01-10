# 普通函数
def add(x, y):
    return x + y


print(add(1, 2))

# 匿名函数
f = lambda x, y: x + y
print(f(1, 2))
# lambda表达式

# 三元表达式
# x > y ? x : y
# python 版本：
# 条件为真的结果 if 判断 else 条件为假的结果
a = 2
b = 1
r = a if a > b else b
print(r)

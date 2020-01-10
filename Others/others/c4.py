# 生成器 Generator
# 打印 0~10000
# yield关键字 yield同样会返回 但函数不会像return一样结束

def gen(m):
    n = 0
    while n <= m:
        n += 1
        yield n


n = (i for i in range(0, 10001))
'''
传统方法耗费资源
for i in n:
    print(i)
'''
g = gen(10000)
# for i in g:
#     print(i)
# print(next(g))
# print(next(g))
# print(next(g))
print(n)

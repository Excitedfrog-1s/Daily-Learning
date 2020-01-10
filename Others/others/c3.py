import copy
# 可迭代对象、迭代器Iterator (能被for in操作)
# 迭代器是个对象
# 迭代器是一次性的
class Book:
    pass

'''
把普通对象变成迭代器
加入__iter__和__next__两个函数
'''
class BookCollection:
    def __init__(self):
        self.data = ['1', '2', '3']
        self.cur = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur >= len(self.data):
            raise StopIteration()  # 抛出异常
        r = self.data[self.cur]
        self.cur += 1
        return r

books = BookCollection()
books_copy = copy.copy(books)  # 浅拷贝
# print(next(books))
# print(next(books))
# print(next(books))
for book in books:
    print(book)
for book in books_copy:
    print(book)

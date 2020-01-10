# coding=utf-8
'''
面向对象
类就像一个模板，产生很多对象
实例化
类的基本作用：封装
方法和函数的区别
方法->设计层面的 函数->运行，过程式的一种称谓
数据成员 变量
实例方法 类方法 静态方法
'''


class Student():
    # 特征 以下为 类变量
    sum = 0  # 班级里学生总数
    name = '123'  # name和age其实没有什么意义
    age = 0

    # 构造函数 必须返回None
    def __init__(self, name, age):
        # 初始化对象的特征 此处实例变量不会覆盖类变量
        self.name = name
        self.age = age
        self.__score = 0
        self.__class__.sum += 1
        print('当前班级学生总数为:' + str(self.__class__.sum))
        # print(self.name) 读取的实例变量
        # print(name) 读取的形参里的name
        # print(Student.sum) 读取类变量
        # print('student')

    # 行为
    def marking(self, score):
        if score < 0:
            return '不能为负数'
        self.__score = score
        print(self.name + '同学的分数为：' + str(self.__score))

    def do_homework(self):  # 实例方法
        self.do_english_homework()  # 内部调用
        print('homework')

    def do_english_homework(self):
        print('')

    @classmethod  # 装饰器
    def plus_sum(cls):  # 类方法
        cls.sum += 1
        print(cls.sum)

    @staticmethod
    def add(x, y):  # 静态方法 没有强制默认传入
        print(Student.sum)
        print('This is a static method')


student1 = Student('A', 18)
student2 = Student('A', 18)

result = student1.marking(59)
print(result)
student1.__score = -1  # __score是新增的实例变量而不是私有变量
print(student1.__dict__)
# print(student1.__score)

# print(student2.__score)
print(student2.__dict__)

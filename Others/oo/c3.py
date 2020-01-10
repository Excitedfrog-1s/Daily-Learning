# coding=utf-8


class Student():
    name = '123'
    age = 0
    sum = 0

    # 实例方法需在参数列表固定放上self
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(age)
        print(name)

    def do_homework(self):
        print('homework')


student1 = Student('A', 18)
student2 = Student('B', 18)
student1.do_homework()
student2.do_homework()
print(student1.__dict__)
print(Student.__dict__)
print(student1.name)
print(Student.name)

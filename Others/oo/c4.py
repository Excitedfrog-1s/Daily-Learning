from c5 import Human


class Student(Human):
    def __init__(self, school, name, age):
        self.school = school
        # Human.__init__(self, name, age)  类调用方法（不推荐）
        super(Student, self).__init__(name, age)

    def do_homework(self):  # 子类方法与父类同名，优先调用子类
        super(Student, self).do_homework()  # 调用父类方法
        print('english homework')


student1 = Student('1', 'A', 18)
student1.do_homework()
# print(student1.sum)
# print(Student.sum)
# print(student1.name)
# print(student1.age)
# student1.get_name()

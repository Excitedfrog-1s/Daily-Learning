# 对象存在不一定为True
# __bool__和__len__


class Test():
    def __bool__(self):
        print('bool')
        return False

    def __len__(self):
        print('len')
        return True  # 0/False


print(len(Test()))
print(bool(Test()))
'''
if test:
    print('S')
else:
    print('F')
'''

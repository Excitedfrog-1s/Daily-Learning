# coding=utf-8
print('a', 'b', 'c')


def demo(param1, param2=2, *param):  # 必须 默认 可变
    print(param1)
    print(param2)
    print(param)
    # print(type(param))


# demo(1, 2, 3, 4, 5, 6)
# a = (1, 2, 3, 4, 5, 6)
demo('a', 1, 2, 3, 'param')

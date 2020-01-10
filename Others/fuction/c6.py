# coding=utf-8


def squsum(*param):
    sum = 0
    for i in param:
        sum += i * i
    print(sum)


squsum(*[1, 2, 3])


# 任意个数的关键字参数
def city_temp(**param):
    for key, value in param.items():
        print(key, ':', value)


a = {'bj': '32c', 'sh': '31c'}
# city_temp(bj='32c', xm='23c', sh='31c')
city_temp(**a)

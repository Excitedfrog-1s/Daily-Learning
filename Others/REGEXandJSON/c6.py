# 正则替换 re.sub
import re

'''
language = 'PythonC#JavaPHP'


def convert(value):
    matched = value.group()
    return '!!' + matched + '!!'


r = re.sub('C#', convert, language, 0)  # count=0表示无限制替换
print(r)
'''

s = 'A8C3721D86'


def convert(value):
    matched = value.group()
    if int(matched) >= 6:
        return '9'
    else:
        return '0'


r = re.sub('\d', convert, s)
print(r)

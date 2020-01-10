# 不同的语言可能会把json转成其他类型
# Python中是转为字典类型
# 由字符串到某一种数据类型 -> 反序列化
# 由数据类型到字符串 -> 序列化

import json

# JSON object array
json_str = '[{"name":"qiyue", "age":18, "flag":false}, {"name":"qiyue", "age":18}]'
student1 = [{
    'name': 'qiyue',
    'age': 18,
    'flag': False
}, {
    'name': 'qiyue',
    'age': 18
}]
student = json.loads(json_str)
json_str2 = json.dumps(student1)
print(type(student))
print(type(json_str2))
print(student)
print(json_str2)
# print(student['name'])
# print(student['age'])

import requests
import re


def getContent(url):
    '''
    获取页面内容
    url：目标网页
    '''
    session = requests.Session()
    content = session.get(url)
    print(content.text)
    return content


def searchKeyValue(method, content):
    '''
    找关键值
    method：匹配规则
    content：待匹配字段
    '''
    key = re.findall(method, content)
    return key


def calculateResult(u0, key1, key2, round, symbol):
    '''
    计算表达式结果
    '''
    i = 0
    if symbol == '+':
        while i < rounds:
            result = (key1 + u0) + (i * key2)
            i += 1
            u0 = result
        return result
    elif symbol == '-':
        while i < rounds:
            result = (key1 + u0) - (i * key2)
            i += 1
            u0 = result
        return result


url = ''
content = getContent(url)
# 初始值
u0 = searchKeyValue('', content.text)
# 表达式中左边括号内的常数
key_1 = searchKeyValue('', content.text)
# 表达式中右边括号内的常数
key_2 = searchKeyValue('', content.text)
# 最终结果需要的轮数
rounds = searchKeyValue('', content.text)
# 两个括号间的计算符号
symbol = searchKeyValue('', content.text)
result = str(calculateResult(u0, key_1, key_2, rounds, symbol))
target_url = '' + result
content_result = getContent(target_url)
print(content_result.text)

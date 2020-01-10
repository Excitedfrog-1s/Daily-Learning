# 基于urllib 更简单
import requests

# 基本GET请求
response = requests.get('https://www.baidu.com/')
print(type(response))
print(response.status_code)
print(type(response.text))
print(response.text)
print(response.cookies)

# 各种请求方式
requests.post('http://httpbin.org/post')
requests.put('http://httpbin.org/put')
requests.delete('http://httpbin.org/delete')
requests.head('http://httpbin.org/get')
requests.options('http://httpbin.org/get')

# 带参数GET请求
data = {'name': 'germany', 'age': 22}
response = requests.get('http://httpbin.org/get', params=data)
print(response)

# 解析JSON
response = requests.get('http://httpbin.org/get')
print(response.json())

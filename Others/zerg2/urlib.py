# Python内置HTTP请求库
# request/error/parse/robotparser
import urllib
import socket
# 请求网页
# GET类型
response = urllib.request.urlopen('http://www.baidu.com')
print(response.read().decode('utf-8'))
# POST类型
data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
response1 = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response1.read())
# ERROR / Time Out
try:
    response2 = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('Time Out')

# 响应
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))
print(response.read().decode('utf-8'))

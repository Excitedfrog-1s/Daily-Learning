import requests
from requests.packages import urllib3
from requests.exceptions import ReadTimeout
# 文件上传
files = {'file': open('cookie.txt', 'rb')}
response = requests.post('http://httpbin.org/post', files=files)
print(response.text)
# 获取Cookie 比urllib方便
response = requests.get('https://www.baidu.com/')
print(response.cookies)
for key, value in response.cookies.items():
    print(key + '=' + value)
# 会话维持
s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
response = s.get('http://httpbin.org/cookies')
print(response.text)
# 证书验证
response = requests.get('https://www.12306.cn/')
urllib3.disable_warnings()
print(response.status_code)
response = requests.get('https://www.12306.cn/', verify=False)
print(response.status_code)
# 超时设置
try:
    response = requests.get('https://www.taobao.com/', timeout=0.1)
    print(response.status_code)
except ReadTimeout:
    print('Time Out')

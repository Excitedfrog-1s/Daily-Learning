# 基本POST请求 添加header信息
import requests
data = {'name': 'germany', 'age': '22'}
headers = {
    "user-agent": ("Mozilla/5.0 (Windows NT"
                   "10.0; Win64; x64) AppleWebKit/537.36 (KHT"
                   "ML, like Gecko) Chrome/70.0.3538.77 Safar"
                   "i/537.36")
}
response = requests.post('http://httpbin.org/post', data=data, headers=headers)
print(response.text)

# 异常处理
from urllib import request, error
import socket
# 请求的网页不存在：
try:
    response = request.urlopen('http://hanliyang.com/index.html')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
except error.URLError as e:
    print(e.reason)
else:
    print('Request Successfully')

# 强制超时：
try:
    response = request.urlopen('http://www.baidu.com', timeout=0.01)
except error.URLError as e:
    print(type(e.reason))
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')

try:
    int('abc')  # ValueError excpet里没有特别定义就会进入最后一行
    file_name = input('文件名：')  # OSError异常
    f = open(file_name)
    print(f.read())
    sum = 1 + '1'  # TypeError异常 此处异常导致close无法执行
except OSError as reason:
    print('文件不存在\n错误原因：' + str(reason))
except TypeError as reason:
    print('类型出错\n错误原因：' + str(reason))
# except (OSError, TypeError):
# print('出错了')
except:
    print('出错了')  # 隐藏错误原因
finally:  # 无论如何都要执行的语句
    f.close()
raise ZeroDivisionError('除数为零的异常')  # 引发异常
 
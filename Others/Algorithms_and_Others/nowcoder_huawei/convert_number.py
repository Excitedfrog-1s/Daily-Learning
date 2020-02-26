def trans(string):
    hex_string = eval(string)
    return hex_string


while True:
    try:
        string = str(input())
        print(trans(string))
    except:
        break

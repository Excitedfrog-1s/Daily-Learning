while True:
    try:
        number = float(input())
        temp = number // 1
        temp_2 = number - temp
        if temp_2 >= 0.5:
            number = int(temp + 1)
        if temp_2 < 0.5:
            number = int(temp)
        print(number)
    except:
        break

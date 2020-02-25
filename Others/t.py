while True:
    try:
        empty_bottle_num = int(input())
        if empty_bottle_num:
            drink_bottle_num = 0
            while empty_bottle_num >= 3:
                temp = empty_bottle_num // 3
                drink_bottle_num += temp
                empty_bottle_num = empty_bottle_num % 3 + temp
            if empty_bottle_num == 2:
                drink_bottle_num += 1
            print(drink_bottle_num)
        else:
            break
    except:
        break

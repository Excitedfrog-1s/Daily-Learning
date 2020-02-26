while True:
    try:
        number_1, number_2 = map(int, input().split())
        if number_1 < number_2:
            temp = number_2
        elif number_2 < number_1:
            temp = number_1
        while True:
            if temp % number_1 == 0 and temp % number_2 == 0:
                gcd = temp
                break
            temp += 1
        print(gcd)
    except Exception:
        exit()

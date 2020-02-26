while True:
    try:
        number = int(input())
        i = 2
        while number != 1:
            for i in range(2, number + 1):
                if number % i == 0:
                    print(str(i), end=' ')
                    number = number // i
                    break
    except:
        break
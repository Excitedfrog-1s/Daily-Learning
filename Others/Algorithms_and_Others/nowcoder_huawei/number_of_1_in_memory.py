while True:
    try:
        number = int(input())
        print(bin(number).count('1'))
    except Exception:
        exit()

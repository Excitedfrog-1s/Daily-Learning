while True:
    try:
        string = input()
        string_set = set(string)
        count = 0
        for i in string_set:
            if ord(i) <= 127:
                count += 1
        print(count)
    except:
        break

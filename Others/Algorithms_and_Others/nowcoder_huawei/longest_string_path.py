while True:
    try:
        number = int(input())
        input_list = []
        if number < 1 or number > 1000:
            raise Exception
        for i in range(number):
            temp = input()
            if len(temp) > 100:
                raise Exception
            if not temp.isalpha():
                raise Exception
            input_list.append(temp)
        input_list.sort()
        for element in input_list:
            print(element)

    except Exception:
        exit()

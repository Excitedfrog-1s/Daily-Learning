while True:
    try:
        new_string = ''
        number = int(input())
        number_string = list(str(number))
        for i in range(len(number_string) - 1, -1, -1):
            if number_string[i] not in new_string:
                new_string = new_string + number_string[i]
        print(new_string)
    except:
        break
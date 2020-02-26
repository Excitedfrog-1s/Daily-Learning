while True:
    try:
        number = int(input())
        count = 0
        array = []
        while count < number:
            temp_number = int(input())
            array.append(temp_number)
            count += 1
        array = list(set(array))
        array.sort()
        for i in array:
            print(i)
    except:
        break

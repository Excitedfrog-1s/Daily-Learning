while True:
    try:
        count = int(input())
        dictionary = {}
        for i in range(count):
            input_list = list(map(int, input().split()))
            current_key = input_list[0]
            current_value = input_list[1]
            if current_key in dictionary:
                new_value = dictionary[current_key] + current_value
                dictionary[current_key] = new_value
            else:
                dictionary[current_key] = current_value
        keys = list(dictionary.keys())
        keys.sort()
        for j in keys:
            value = dictionary[j]
            print(str(j) + ' ' + str(value))
    except:
        break

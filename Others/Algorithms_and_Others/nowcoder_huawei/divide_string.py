def split_string(string):
    new_string_list = []

    while len(string) > 8:
        temp = string[0:8]
        string = string[8:]
        new_string_list.append(temp)

    if len(string) <= 8:
        new_string_list.append(string + '0' * (8 - len(string)))
        return new_string_list


string_1 = str(input())
string_2 = str(input())
string_1_list = split_string(string_1)
string_2_list = split_string(string_2)
for i in string_1_list:
    print(i)
for i in string_2_list:
    print(i)

#!/usr/bin/env python
# coding: utf-8

'''
This is the code to transform data to 1/-1 format
The addresses of virtual machines used for data capture
'''

source_address = [
    '02|6c|86|2d|64|0a', '02|9a|33|93|e3|7e', '02|d2|7e|62|db|f6',
    '0a|60|cf|67|df|22', '0a|70|db|2a|d1|86', '0a|a2|9c|66|c3|0c',
    '0a|12|b6|0f|d9|14', '0a|2a|fb|be|7b|40', '0a|15|da|57|7d|d6',
    '0a|19|cc|6a|9e|46', '0a|2c|0f|86|98|08', '0a|67|d5|a5|45|20',
    '0a|d4|65|8d|21|9c', '0a|13|9c|24|86|32', '0a|5f|60|81|86|3a',
    '0a|24|7b|18|a6|4c', '0a|74|12|a9|8a|4e', '0a|f7|54|81|87|20',
    '0a|50|04|a8|21|90', '0a|ac|2b|30|f3|be', '0a|2f|3e|28|cb|4e',
    '0a|ee|94|0f|c1|68', '0a|55|50|8d|45|3a', '0a|4c|b7|2b|cd|cc',
    '0a|f3|3e|a9|44|b0'
]
# The file path of data file
file_path = 'data/Wikipedia1.txt'


def hexstr_to_int(hexstr):
    index = 1
    int_num = 0
    for dig in hexstr:
        if ord(dig) < 97:
            int_num = int_num + pow(16, len(hexstr) - index) * (ord(dig) - 48)
        else:
            int_num = int_num + pow(16, len(hexstr) - index) * (ord(dig) - 87)
        index = index + 1
    return int(int_num)


def data_transform(list_TLSlength):
    data_transformed = []
    for length in list_TLSlength:
        l = length
        negative = 1
        if l < 0:
            negative = -1
            l = -l
        while l >= 512:
            l = l - 512
            data_transformed.append(negative)
        if len(data_transformed) >= 5000:
            break

    if len(data_transformed) < 5000:
        data_transformed = data_transformed + [0] * (5000 -
                                                     len(data_transformed))
    return data_transformed[:5000]


TLSlength = []
with open(file_path) as f:
    p = 0
    first_line = False
    for line in f.readlines():
        p = p + 1
        if p == 100000:
            break
        if line[-6:-1] == 'ETHER':
            first_line = True
            continue
        elif first_line == True:
            nega = -1
            if '|17|03|03|' in line:
                first_part = line.split('|17|03|03|')[0]

                if first_part[24:41] in source_address:
                    nega = 1

                second_part = line.split('|17|03|03|')[1]
                list_nums = second_part.split('|')[0:2]

                first_line = False
                if len(list_nums) == 2:
                    TLSlength.append(
                        nega * hexstr_to_int(list_nums[0] + list_nums[1]))
        else:
            continue
datad = data_transform(TLSlength)
print(datad)
print(len(datad))

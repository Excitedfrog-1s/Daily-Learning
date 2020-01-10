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
            l = -1
        while l >= 512:
            l = l - 512
            data_transformed.append(negative)
    return data_transformed


TLSlength = []
with open('F:\VSProjects\VSCode\Python\Capstone\cw_datasets\wireshark.txt') as f:
    p = 0
    first_line = False
    for line in f.readlines():
        p = p + 1
        if p == 1000:
            break
        if line[-6:-1] == 'ETHER':
            first_line = True
            continue
        elif first_line == True:
            nega = 1
            if '|17|03|03|' in line:
                first_part = line.split('|17|03|03|')[0]
                if first_part[6:23] == '44|85|00|cf|70|2e':
                    nega = -1
                second_part = line.split('|17|03|03|')[1]
                lsit_nums = second_part.split('|')[0:2]
            first_line = False
            TLSlength.append(nega * hexstr_to_int(lsit_nums[0] + lsit_nums[1]))
        else:
            continue
print(data_transform(TLSlength))

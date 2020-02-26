string = str(input())
length = 0
for i in string[-1::-1]:
    if i != ' ':
        length += 1
    else:
        break
print(length)

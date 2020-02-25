string = str(input()).lower()
character = str(input()).lower()
count = 0
for i in string:
    if i == character:
        count += 1
print(count)

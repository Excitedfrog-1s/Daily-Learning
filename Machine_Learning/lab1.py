word_list = ['arts', 'rats', 'star', 'tars', 'start', \
            'pat', 'allergy', 'lager', 'largely', 'regally', \
            'apt', 'potters', 'tap', 'bluest', 'tap', 'bluets', \
            'retraced', 'gallery','bustle', 'sublet', 'subtle', 'grab']

def find_key(i):
    key = list(i)
    key.sort()
    key = ''.join(key)
    return key

def update(a, key, i):
    if key in a.keys():
        if i not in a[key]:
            a[key].append(i)
    else:
        a[key] = [i]

# Main
a = {}
for i in word_list:
    key = find_key(i)
    update(a, key, i)
print(a)

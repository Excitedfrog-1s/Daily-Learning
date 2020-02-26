while True:
    try:
        sentence = list(input().split())[::-1]
        print(' '.join(sentence))
    except:
        break

while True:
    try:
        string = input()
        if len(string) > 1000:
            print("String too long")
            break
        print(string[::-1])
    except:
        break

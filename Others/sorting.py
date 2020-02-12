k = [7, 4, 1, 5, 2, 8, 0, 3, 6, 9]


def straightInsertionSortAscending(array):
    '''
    直接插入排序升序
    '''
    for i in range(1, len(k)):
        if k[i] < k[i - 1]:
            temp = k[i]
            j = i - 1
        while k[j] > temp and j >= 0:
            k[j + 1] = k[j]
            j -= 1
        k[j + 1] = temp
    print(k)


def straightInsertionSortDescending(array):
    '''
    直接插入排序降序
    '''
    for i in range(1, len(k)):
        if k[i] > k[i - 1]:
            temp = k[i]
            j = i - 1
        while k[j] < temp and j >= 0:
            k[j + 1] = k[j]
            j -= 1
        k[j + 1] = temp
    print(k)


def bubbleSortAscending(array):
    '''
    冒泡排序升序
    '''


straightInsertionSortAscending(k)
straightInsertionSortDescending(k)

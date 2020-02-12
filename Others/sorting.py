def straightInsertionSortAscending(array):
    '''
    直接插入排序升序
    '''
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            temp = array[i]
            j = i - 1
        while array[j] > temp and j >= 0:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = temp
    print(array)


def straightInsertionSortDescending(array):
    '''
    直接插入排序降序
    '''
    for i in range(1, len(array)):
        if array[i] > array[i - 1]:
            temp = array[i]
            j = i - 1
        while array[j] < temp and j >= 0:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = temp
    print(array)


def bubbleSortAscending(array):
    '''
    冒泡排序升序
    '''
    for i in range(1, len(array)):
        flag = 0
        for j in range(len(array) - i):
            if array[j] > array[j + 1]:
                temp = array[j + 1]
                array[j + 1] = array[j]
                array[j] = temp
                flag = 1
            j += 1
        i += 1
        if flag == 0:
            break
    print(array)


def bubbleSortDescending(array):
    '''
        冒泡排序降序
        '''
    for i in range(1, len(array)):
        flag = 0
        for j in range(len(array) - i):
            if array[j] < array[j + 1]:
                temp = array[j + 1]
                array[j + 1] = array[j]
                array[j] = temp
                flag = 1
            j += 1
        i += 1
        if flag == 0:
            break
    print(array)


def quickSortAscendingFirstRound(array, low, high):
    '''
    快速排序升序第一轮
    '''
    key = array[low]
    while low < high:
        while low < high and array[high] >= key:
            high -= 1
        array[low] = array[high]
        while low < high and array[low] <= key:
            low += 1
        array[high] = array[low]
    array[low] = key
    return low


def quickSortAscending(array, low, high):
    '''
    快速排序升序
    '''
    if low < high:
        basepoint = quickSortAscendingFirstRound(array, low, high)
        quickSortAscending(array, low, basepoint - 1)
        quickSortAscending(array, basepoint + 1, high)
    return array


def quickSortDescendingFirstRound(array, low, high):
    '''
    快速排序降序第一轮
    '''
    key = array[low]
    while low < high:
        while low < high and array[high] <= key:
            high -= 1
        array[low] = array[high]
        while low < high and array[low] >= key:
            low += 1
        array[high] = array[low]
    array[low] = key
    return low


def quickSortDescending(array, low, high):
    '''
    快速排序降序
    '''
    if low < high:
        basepoint = quickSortDescendingFirstRound(array, low, high)
        quickSortDescending(array, low, basepoint - 1)
        quickSortDescending(array, basepoint + 1, high)
    return array


if __name__ == '__main__':
    array = [4, 2, 3, 6, 5, 1, 9, 7, 0, 8]
    # straightInsertionSortAscending()
    # straightInsertionSortDescending()
    # bubbleSortAscending()
    # bubbleSortDescending()
    print(quickSortAscending(array, 0, len(array) - 1))
    print(quickSortDescending(array, 0, len(array) - 1))

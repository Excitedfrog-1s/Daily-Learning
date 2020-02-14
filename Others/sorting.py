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


def createSmallHeap(array, root, size):
    '''
    堆排序，保证以root为根的堆是小根堆，用于降序排序
    root: 起始点
    size：堆大小
    '''
    left_child = root * 2 + 1
    right_child = root * 2 + 2
    new_root = root
    if left_child < size and array[new_root] > array[left_child]:
        new_root = left_child
    if right_child < size and array[new_root] > array[right_child]:
        new_root = right_child
    if new_root != root:
        array[new_root], array[root] = array[root], array[new_root]
        createSmallHeap(array, new_root, size)
    return array


def createBigHeap(array, root, size):
    '''
    堆排序，保证以root为根的堆是大根堆，用于升序排序
    root: 起始点
    size：堆大小
    '''
    left_child = root * 2 + 1
    right_child = root * 2 + 2
    new_root = root
    if left_child < size and array[new_root] < array[left_child]:
        new_root = left_child
    if right_child < size and array[new_root] < array[right_child]:
        new_root = right_child
    if new_root != root:
        array[new_root], array[root] = array[root], array[new_root]
        createBigHeap(array, new_root, size)
    return array


def buildSmallHeap(array):
    '''
    建小根堆
    '''
    size = len(array)
    for i in range((size - 2) // 2, -1, -1):
        createSmallHeap(array, i, size)
    return array


def buildBigHeap(array):
    '''
    建大根堆
    '''
    size = len(array)
    for i in range((size - 2) // 2, -1, -1):
        createBigHeap(array, i, size)
    return array


def heapSortAscending(array):
    '''
    堆排序升序
    '''
    array = buildBigHeap(array)
    for i in range(len(array) - 1, -1, -1):
        array[0], array[i] = array[i], array[0]
        createBigHeap(array, 0, i)
    print(array)


def heapSortDescending(array):
    '''
    堆排序降序
    '''
    array = buildSmallHeap(array)
    for i in range(len(array) - 1, -1, -1):
        array[0], array[i] = array[i], array[0]
        createSmallHeap(array, 0, i)
    print(array)


def twoWayMerge(array, start, middle, end):
    '''
    将两个有序表归并为一个升序有序表
    a: 标识第一个序列的位置
    b: 标识第二个序列的位置
    c: 新序列的位置
    '''
    first_array_end = middle - start + 1
    second_array_end = end - middle
    first_array = [None] * first_array_end
    second_array = [None] * second_array_end
    a, b, c = 0, 0, start
    for i in range(0, first_array_end):
        first_array[i] = array[start + i]
    for j in range(0, second_array_end):
        second_array[j] = array[middle + j + 1]
    while a != first_array_end and b != second_array_end:
        # 降序只需将下行改为 >=
        if first_array[a] <= second_array[b]:
            array[c] = first_array[a]
            c += 1
            a += 1
        else:
            array[c] = second_array[b]
            b += 1
            c += 1
    while a < first_array_end:
        array[c] = first_array[a]
        a += 1
        c += 1
    while b < second_array_end:
        array[c] = second_array[b]
        b += 1
        c += 1

    return array


def twoWayMergeSort(array, start, end):
    '''
    二路归并排序
    '''
    if start < end:
        middle = (start + end) // 2
        twoWayMergeSort(array, start, middle)
        twoWayMergeSort(array, middle + 1, end)
        twoWayMerge(array, start, middle, end)
        return array


if __name__ == '__main__':
    array = [4, 2, 5, 6, 3, 1, 9, 7, 0, 8]
    straightInsertionSortAscending(array)
    straightInsertionSortDescending(array)
    bubbleSortAscending(array)
    bubbleSortDescending(array)
    print(quickSortAscending(array, 0, len(array) - 1))
    print(quickSortDescending(array, 0, len(array) - 1))
    heapSortAscending(array)
    heapSortDescending(array)
    print(twoWayMergeSort(array, 0, len(array) - 1))

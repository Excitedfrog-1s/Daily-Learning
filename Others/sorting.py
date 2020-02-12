class Sorting:

    def __init__(self, array):
        self.array = array

    def straightInsertionSortAscending(self):
        '''
        直接插入排序升序
        '''
        for i in range(1, len(self.array)):
            if self.array[i] < self.array[i - 1]:
                temp = self.array[i]
                j = i - 1
            while self.array[j] > temp and j >= 0:
                self.array[j + 1] = self.array[j]
                j -= 1
            self.array[j + 1] = temp
        print(self.array)

    def straightInsertionSortDescending(self):
        '''
        直接插入排序降序
        '''
        for i in range(1, len(self.array)):
            if self.array[i] > self.array[i - 1]:
                temp = self.array[i]
                j = i - 1
            while self.array[j] < temp and j >= 0:
                self.array[j + 1] = self.array[j]
                j -= 1
            self.array[j + 1] = temp
        print(self.array)

    def bubbleSortAscending(self):
        '''
        冒泡排序升序
        '''
        for i in range(1, len(self.array)):
            flag = 0
            for j in range(len(self.array) - i):
                if self.array[j] > self.array[j + 1]:
                    temp = self.array[j + 1]
                    self.array[j + 1] = self.array[j]
                    self.array[j] = temp
                    flag = 1
                j += 1
            i += 1
            if flag == 0:
                break
        print(self.array)

    def bubbleSortDescending(self):
        '''
            冒泡排序降序
            '''
        for i in range(1, len(self.array)):
            flag = 0
            for j in range(len(self.array) - i):
                if self.array[j] < self.array[j + 1]:
                    temp = self.array[j + 1]
                    self.array[j + 1] = self.array[j]
                    self.array[j] = temp
                    flag = 1
                j += 1
            i += 1
            if flag == 0:
                break
        print(self.array)
    
    def quickSortAscending(self):
        '''
        快速排序升序
        '''


x = Sorting([4, 2, 3, 6, 5, 1, 9, 7, 0, 8])
x.straightInsertionSortAscending()
x.straightInsertionSortDescending()
x.bubbleSortAscending()
x.bubbleSortDescending()

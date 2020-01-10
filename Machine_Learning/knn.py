#coding=utf-8
# 参考https://www.cnblogs.com/ybjourney/p/4702562.html进行的初次KNN验证
from numpy import *
import matplotlib.pyplot as plt
import operator


#训练集
def DataSet():
    #A类为第一个小于1第二个大于1，B类相反
    group = array([[3, 104], [2, 100], [1, 81], [101, 10], [99, 5], [81, 2]])
    labels = ['A', 'A', 'A', 'B', 'B', 'B']
    return group, labels


# 画个图
def DrawPic():
    x1 = array([3, 2, 1])
    y1 = array([104, 100, 81])
    x2 = array([101, 99, 98])
    y2 = array([10, 5, 2])
    x = array([18])
    y = array([90])
    scatter1 = plt.scatter(x1, y1, c='r')
    scatter2 = plt.scatter(x2, y2, c='b')
    scatter3 = plt.scatter(x, y, c='k')
    plt.legend(
        handles=[scatter1, scatter2, scatter3],
        labels=['labelA', 'labelB', 'X'],
        loc='best')
    plt.show()


#计算欧氏距离
def Distance(inputData, dataSet):
    dataSize = dataSet.shape[0]
    diff = tile(inputData, (dataSize, 1)) - dataSize
    sqdiff = diff**2
    squareDist = sum(sqdiff, axis=1)
    dist = squareDist**0.5
    sortedDistIndex = argsort(dist)
    return sortedDistIndex


#KNN分类
def Classify(sortedDistIndex, label, k):
    classCount = {}
    for i in range(k):
        voteLabel = label[sortedDistIndex[i]]
        classCount[voteLabel] = classCount.get(voteLabel, 0) + 1
    maxCount = 0
    for key, value in classCount.items():
        if value > maxCount:
            maxCount = value
            classes = key
    return classes


#Main
dataSet, labels = DataSet()
inputData = array([18, 90])  #测试数据
DrawPic()
K = 3
sortedDistIndex = Distance(inputData, dataSet)
output = Classify(sortedDistIndex, labels, K)
print("数据：", inputData, "结果：", output)

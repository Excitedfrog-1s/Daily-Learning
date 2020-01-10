import numpy as np
import matplotlib.pylab as pl

X = np.asarray(([2, 1, 3, 5, 3, 10, 9, 5, 8, 11, 15, 13, 16],
                [1, 0, 3, 5, 2, 12, 11, 10, 7, 9, 11, 15, 16])).T
y = np.asarray([0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2])[:, np.newaxis]
print('X=\n', X)
print('y=\n', y)
N = len(y)
X_q = np.asarray(([4.5], [5])).T  #query point
pos_of_class0 = np.where(y == 0)[0]  #class 0 points
pos_of_class1 = np.where(y == 1)[0]  #class 1 points
pos_of_class2 = np.where(y == 2)[0]  #class 2 points
pl.scatter(
    X[pos_of_class0, 0], X[pos_of_class0, 1], c='r', edgecolor='')  #class = 0
pl.scatter(
    X[pos_of_class1, 0], X[pos_of_class1, 1], c='g', edgecolor='')  #class = 1
pl.scatter(
    X[pos_of_class2, 0], X[pos_of_class2, 1], c='b', edgecolor='')  #class = 2
pl.scatter(
    X_q[:, 0], X_q[:, 1], marker='*', s=100, c='k',
    edgecolor='')  #class to be determined
for i in range(N):
    pl.scatter(
        X[i, 0] + 0.4, X[i, 1] - 0.5, s=100,
        marker="$ {} $".format(i))  #positions
dis = ((X - X_q)**2).sum(
    axis=1)  #calculate distance between X_q and each training point
arg_ascending = np.argsort(dis)  #arrange distances in the ascending order

np.set_printoptions(precision=3)
print('Distance between X_q and each training point= \n', dis)
print('Index of nearest neighbors in training data=\n',
      arg_ascending)  #Check the plot in Step 1
K = 5  #Let us consider 5-nearest neighbors

classes = np.zeros(3)
for i in range(K):
    if y[arg_ascending[i]] == 0:  #class = 0
        print(i, 'th nearest neighbor belongs to class 0.')
        classes[0] += 1
    elif y[arg_ascending[i]] == 1:  #class = 1
        print(i, 'th nearest neighbor belongs to class 1.')
        classes[1] += 1
    elif y[arg_ascending[i]] == 2:  #class = 2
        print(i, 'th nearest neighbor belongs to class 2.')
        classes[2] += 1
    else:
        print('Error - Invalid class')

prob = classes / K
print('classes', classes)
print('probabilities=', prob)
print('ANSWER: X_q blongs to', np.argmax(classes), 'th class!')

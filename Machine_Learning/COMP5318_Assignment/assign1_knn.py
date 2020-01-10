import time
from collections import Counter
import h5py
import numpy as np
from scipy.spatial import KDTree
from matplotlib import pyplot as plt

start_time = time.time()


def load_trainingdata():
    '''
    Loading data from training set
    Please change path at first
    '''
    path = 'F:/VSProjects/VSCode/Python/machine_learning/'
    with h5py.File(path + 'images_training.h5', 'r') as H:
        data = np.copy(H['data'])
    with h5py.File(path + 'labels_training.h5', 'r') as H:
        label = np.copy(H['label'])
    return data, label


def load_testingdata():
    '''
    Loading data from testing set
    Please change path at first
    '''
    path = 'F:/VSProjects/VSCode/Python/machine_learning/'
    with h5py.File(path + 'images_testing.h5', 'r') as H:
        data_t = np.copy(H['data'])
    with h5py.File(path + 'labels_testing_2000.h5', 'r') as H:
        label_t = np.copy(H['label'])
    return data_t, label_t


def normalization(data):
    '''
    Preprocessing data: Normalization
    '''
    data = np.array([x / np.amax(x) for x in data])
    return data


def flat(data):
    """
    Flatten images in the data array
    """
    return data.reshape(data.shape[0], data.shape[1]**2)


def PCA(data, n_components):
    '''
    Principal Component Analysis
    x: Data after zero-meam, shape is 35000 * 784
    s: Covariance matrix, shape is 784 * 784
    l: Array of eigenvalues, shape is 784 * 1
    v: Matrix of eigenvectors, shape is 784 * 784
    x_pca: Data after dimension reduction, shape is 35000 * 30
    '''
    n = n_components
    data = data
    x = data - np.mean(data, axis=0)
    s = np.cov(x.T)
    l, v = np.linalg.eig(s)
    # Sort eigenvectors by descending order on eigenvalues
    v = v[:, np.argsort(-l)][:, :n]
    # Sort eigenvalues by descending order
    l = -np.sort(-l)[:n]
    x_pca = v.T @ x.T
    x_pca = x_pca.T
    return x_pca


def KNN(data_pca, label, data_t_pca, k):
    '''
    K Nearest Neighbour Classfier with K-Dimensional Tree
    '''
    tree = KDTree(data_pca)
    dist, indices = tree.query(data_t_pca, k)
    predicted = np.array([
        Counter(label[indices[n]]).most_common(1)[0][0]
        for n in range(data_t_pca.shape[0])
    ])
    return predicted


def accuracy(label_t, predicted):
    '''
    Calculate the accuracy of this classifier
    '''
    num = np.sum(predicted == label_t)
    acc = num / len(label_t)
    return num, acc


# Load and normalize data
data, label = load_trainingdata()
data_t, label_t = load_testingdata()
data = normalization(data)
data_t = normalization(data_t)
# d contains both training and test dataset. Shape is 35000 * 784
d = np.append(flat(data), flat(data_t), axis=0)
'''
Use in determine the best K and PCA value, remove annotation when determine PCA
mid_time = time.time()
mid = mid_time - start_time
'''

# PCA on data
x_pca = PCA(d, 30)
data_pca = x_pca[:data.shape[0]]
data_t_pca = x_pca[-data_t.shape[0]:]

# KNN
predicted = KNN(data_pca, label, data_t_pca, 9)

# Accuracy
num, acc = accuracy(label_t, predicted[:2000])
print('The number of correct prediction is:', num, '\n'
      'The accuracy is:', acc)

# Output
with h5py.File('predicted_labels.h5', 'w') as H:
    H.create_dataset('label', data=predicted)

# Time
end_time = time.time()
t = end_time - start_time
print('Running time is:', round(t, 4), 's')
'''
This cell is to calculate accuracies and times, which will be used to determine best PCA value
PCA_values = [1, 5, 10, 20, 25, 30, 35, 50, 100]
k_values = [2, 5, 9, 10, 11, 15, 20, 50, 100]

for i in PCA_values:
    pca_time = time.time()
    X_PCA = PCA(d, i)
    data_pca = X_PCA[:data.shape[0]]
    data_t_pca = X_PCA[-data_t.shape[0]:]
    pca_final_time = time.time() - pca_time
    for j in k_values:
        knn_time = time.time()
        predicted = KNN(data_pca, label, data_t_pca, j)
        num, acc = accuracy(label_t, predicted[:2000])
        print('PCA Value: %d and K Value: %d' % (i, j))
        print('Accuracy:', acc)
        end_time = time.time()
        t = (end_time - knn_time) + mid + pca_final_time
        print('Time:', round(t, 4), 's')
'''
'''
This cell is to draw a picture about accuracies and PCAs
acc_values = [0.267, 0.735, 0.798, 0.829, 0.837, 0.839, 0.839, 0.841, 0.837]
plt.grid(True)
plt.xlabel('PCA Values')
plt.ylabel('Average Accuracy')
plt.title('Accuracy with Different PCAs')
plt.scatter(PCA_values, acc_values, c='r')
plt.show()
'''
'''
This cell is to draw a picture about times and PCAs
time_values = [2.15, 7.16, 24.78, 62.50, 76.02, 88.12, 104.02, 132.48, 211.92]
plt.grid(True)
plt.xlabel('PCA Values')
plt.ylabel('Average Time')
plt.title('Time with Different PCAs')
plt.scatter(PCA_values, time_values, c='r')
plt.show()
'''
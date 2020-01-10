import math
import random
import numpy as np
import matplotlib.pyplot as pl
from scipy import misc

# Defining numpy arrays
x_list = np.array([1, 2, 3, 6, 9, 13])
print(x_list)
print(x_list[0])
print(x_list[1:-2])
# Numpy operations and slicing
y1_list = [2 * x_i for x_i in x_list]
y2_list = [x_i**2 + 2 * x_i + 1 for x_i in x_list]
y3_list = [math.log10(x_i) for x_i in x_list]
y4_list = [x_i > 4 for x_i in x_list]
print('-----' * 10)
print('x_list = ', x_list)
print('y1_list = ', y1_list)
print('y2_list = ', y2_list)
print('y3_list = ', y3_list, '\n and rounded y3_list = ',
      [round(y3_i, 4) for y3_i in y3_list])
print('y4_list = ', y4_list)
print('-----' * 10)
# Generate a numpy sequence
x = np.arange(0, 10, 2)
y = np.arange(0, 10)
print(x, y)
print('-----' * 10)
a = 1
b = np.arange(5, 12)
c = 1
for i in b:
    delta = np.sqrt(i**2 - 4 * a * c)
    print('b = ', i)
    print('Positive: ', np.round(((-i + delta) / (2 * a)), 2))
    print('Negative: ', np.round(((-i - delta) / (2**a)), 2))
print('-----' * 10)
t = np.arange(501) / 50
f = 1
y2 = np.sin(2 * np.pi * f * t) * np.exp(-t / 2)
pl.scatter(t, y2)
pl.show()
print('-----' * 10)
# Matrix operaions
A = np.array([1, 2, 3])
B = np.array([[1, 2, 3]])
C = np.array([[1, 2, 3], [4, 5, 6]])
D = np.array([[1, 2, 3], [3, 5, 6], [2, 8, 11]])
E = np.array([[2, 0], [4, 1], [1, 2]])
F = np.array([[4, 2, 11, 3]])
print('A = \n {}'.format(A))
print('shape of A is {}'.format(A.shape))
print('B = \n {}'.format(B))
print('shape of B is {}'.format(B.shape))
print('C = \n {}'.format(C))
print('shape of C is {}'.format(C.shape))
print('D = \n {}'.format(D))
print('shape of D is {} \n'.format(D.shape))
print('E = \n {}'.format(E))
print('shape of E is {} \n'.format(E.shape))
print('F = \n {}'.format(F))
print('shape of F is {} \n'.format(F.shape))
Et = E.T
print('Transpose of E is \n {} \n'.format(Et))
E1C = E.T * C
print('Et * C is \n {} \n'.format(E1C))
EC = E.dot(C)
print('E * C is \n {} \n'.format(EC))
BtF = B.T.dot(F)
print('Bt * F is \n {} \n'.format(BtF))
AtF = A[np.newaxis, :].T.dot(F)
print('At * F is \n {} \n'.format(AtF))
# Matrix decomposition using numpy
A2 = np.diag((1, 2, 3))
print(A2)
Q, R = np.linalg.qr(A2)
print('Q = \n', np.round(Q, 2))
print('R = \n', np.round(R, 2))
n, o = np.linalg.eig(A2)
print('Eigenvalue is: \n', n)
print('Eigenvector is: \n', o)
print((A2 - np.eye(A2.shape[0])).dot(o))
print(o.T.dot(o))
print('-----' * 10)
# Singular value decomposition
H = np.array([[1, 1, 1, 0, 0],\
              [3, 3, 3, 0, 0],\
              [4, 4, 4, 0, 0],\
              [5, 5, 5, 0, 0],\
              [0, 2, 0, 4, 4],\
              [0, 0, 0, 5, 5],\
              [0, 1, 0, 2, 2]])
U, s, Vt = np.linalg.svd(H, full_matrices=False)
S = np.diag(s)
print('U = {} \n\n s = {} \n\n Vt = {} \n\n'.format(
    np.round(U, 2), np.round(S, 2), np.round(Vt, 2)))
H_2 = U.dot(S.dot(Vt))
print('H_2 = {}'.format(np.round(H_2, 2)))
print('Is H close to H_2?', np.allclose(H, H_2))
print('-----' * 10)
print('Rank of H is:', np.linalg.matrix_rank(H))
for n in range(1, S.shape[0]):
    reconstruct = U[0:U.shape[0], 0:n].dot(S[0:n, 0:n]).dot(
        Vt[0:n, 0:Vt.shape[1]])
    ratio = n / H.shape[1]
    compression = (H.shape[1] * n + n + H.shape[0] * n) / (
        H.shape[1] * H.shape[0])
    print(
        'Dominant SVD is {} \n Reconstructd matirx is \n {} \n Compression Ratio is \n {} \n'
        .format(n, np.round(reconstruct, 3), np.round(compression, 10)))
print('-----' * 10)
H = misc.face(gray=True)
n = random.randint(0, 500)
U, s, Vt = np.linalg.svd(H, full_matrices=False)
S = np.diag(s)
reconstruct = U[0:U.shape[0], 0:n].dot(S[0:n, 0:n]).dot(Vt[0:n, 0:Vt.shape[1]])
compression = (H.shape[1] * n + n + H.shape[0] * n) / (H.shape[1] * H.shape[0])
pl.figure()
pl.imshow(H)
pl.title('Original Image')
pl.show()
pl.imshow(reconstruct)
pl.title('Compressed Image')
pl.show()
print(
    'Dominant SVD is {} \n Reconstructd matirx is \n {} \n Compression Ratio is \n {} \n'
    .format(n, np.round(reconstruct, 3), np.round(compression, 10)))

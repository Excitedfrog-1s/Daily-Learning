# SVD Reconstruct from lab2
import random
import numpy as np
import matplotlib.pyplot as pl
from scipy import misc


# Random array
def Generate_Array():
    Array = np.random.randint(0, 100, (6, 6))
    return Array


# SVD function
def SVD(Array):
    U, s, Vt = np.linalg.svd(Array, full_matrices=False)
    S = np.diag(s)
    return U, S, Vt


# Matrix reconstruction
def MR(U, S, Vt):

    # Decide how many SVD values will be in used
    n = random.randint(0, 200)
    R = U[0:U.shape[0], 0:n].dot(S[0:n, 0:n]).dot(Vt[0:n, 0:Vt.shape[1]])
    return n, R


# Compute compression rate
def Compreesion_Rate(Array, n):
    compression = (Array.shape[1] * n + n + Array.shape[0] * n) / (
        Array.shape[1] * Array.shape[0])
    return compression


# Draw pictures before and after compression
def Draw(image, R):
    pl.figure()
    pl.imshow(image)
    pl.title('Original Image')
    pl.show()
    pl.imshow(R)
    pl.title('Compressed Image')
    pl.show()


# Main
Array = Generate_Array()
U, S, Vt = SVD(Array)
n, R = MR(U, S, Vt)
C = Compreesion_Rate(Array, n)
print(
    'Dominant SVD is {} \n Reconstructd matirx is \n {} \n Compression Ratio is \n {} \n'
    .format(n, np.round(R, 3), np.round(C, 10)))
print('-----' * 10)
Image = misc.face(gray=True)
U, S, Vt = SVD(Image)
n, R = MR(U, S, Vt)
Draw(Image, R)

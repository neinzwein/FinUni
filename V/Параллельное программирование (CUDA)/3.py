# 3. С использованием инструментария CUDA напишите программу, вычисляющую сумму двух произвольных матриц на GPU.

import numpy as np
from numba import cuda

# https://numba.pydata.org/numba-doc/dev/cuda/examples.html
#Хуже UFunc в 2 раза
@cuda.jit
def matrix_addiction(A, B, C):
    i, j = cuda.grid(2)
    if i < A.shape[0] and j < A.shape[1]:
        C[i, j] = A[i, j] + B[i, j]

n, m = 8, 8
A = np.random.randn(n, m).astype(np.float32)
B = np.random.randn(n, m).astype(np.float32)
C = np.zeros_like(A).astype(np.float32)

# сетка потоков.
# https://www.youtube.com/watch?v=9bBsvpg-Xlk&ab_channel=nickcorn93
# threadsperblock = (16, 16)
# blockspergrid_x = int(np.ceil(A.shape[0] / threadsperblock[0]))
# blockspergrid_y = int(np.ceil(A.shape[1] / threadsperblock[1]))
# blockspergrid = (blockspergrid_x, blockspergrid_y)

# matrix_addition[blockspergrid, threadsperblock](A, B, C)

# автоматическая сетка потоков
matrix_addiction[(n,m),(1,1)](A,B,C)
# print(A)
# print(B)
print(C)
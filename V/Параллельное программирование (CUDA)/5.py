# 5. С использованием инструментария CUDA напишите программу, вычисляющую произведение двух произвольных матриц на GPU.

import numpy as np
from numba import cuda, float32

@cuda.jit
def matmul(A, B, C):
    i, j = cuda.grid(2)
    if i < C.shape[0] and j < C.shape[1]:
        tmp = 0.
        for k in range(A.shape[1]):
            tmp += A[i, k] * B[k, j]
        C[i, j] = tmp

n,m =1024,1024
A = np.random.rand(n,m).astype(np.float32)
B = np.random.rand(n,m).astype(np.float32)
C = np.zeros_like(A).astype(np.float32)

matmul[(n,m),(1,1)](A,B,C)
print(C)

# ниже пример с сайта. Он значительно быстрее. (с предзагрузкой данных в общую память и синхронизацией потоков на блоках)

# TPB = 16

# @cuda.jit
# def fast_matmul(A, B, C):
#     # Define an array in the shared memory
#     # The size and type of the arrays must be known at compile time
#     sA = cuda.shared.array(shape=(TPB, TPB), dtype=float32)
#     sB = cuda.shared.array(shape=(TPB, TPB), dtype=float32)

#     x, y = cuda.grid(2)

#     tx = cuda.threadIdx.x
#     ty = cuda.threadIdx.y
#     bpg = cuda.gridDim.x # блоки на сетку

#     if x >= C.shape[0] and y >= C.shape[1]:
#         # в примере из сайта сказано, что данный алгоритм рассчитан на квадратные матрицы.
#         return

#     # TPB - длина вектора в результате(в ячейке матрицы как я понял)
#     tmp = 0.
#     for i in range(bpg):
#         # Preload data into shared memory
#         sA[tx, ty] = A[x, ty + i * TPB]
#         sB[tx, ty] = B[tx + i * TPB, y]

#         cuda.syncthreads() # ожидание окончания загрузки в общую память

#         for j in range(TPB):
#             tmp += sA[tx, j] * sB[j, ty]

#         cuda.syncthreads() # ожидание окончания перемножения

#     C[x, y] = tmp

# n,m = 1024,1024
# A = np.random.rand(n,m).astype(np.float32)
# B = np.random.rand(n,m).astype(np.float32)
# C = np.zeros_like(A).astype(np.float32)

# threadsperblock = (TPB, TPB)
# blockspergrid_x = int(np.ceil(n / threadsperblock[0]))
# blockspergrid_y = int(np.ceil(m / threadsperblock[1]))
# blockspergrid = (blockspergrid_x, blockspergrid_y)

# fast_matmul[blockspergrid, threadsperblock](A, B, C)

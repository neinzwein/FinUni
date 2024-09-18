# 4. С использованием инструментария CUDA напишите программу, вычисляющую скалярное произведение двух произвольных векторов на GPU.

import numpy as np
from numba import cuda

# скалярное произведение векторов - это сумма умножений по i-тым его элементов.
# https://numba.pydata.org/numba-doc/0.50.0/cuda/intrinsics.html
@cuda.jit
def scalar_vector_multiply(A:np.ndarray,B:np.ndarray,result:np.ndarray)->np.ndarray:
    i=cuda.grid(1)
    if i< A.size:
        cuda.atomic.add(result,0,A[i]*B[i])

n = 1024
A = np.random.randn(n).astype(np.float32)
B = np.random.randn(n).astype(np.float32)

result = np.zeros(shape=1).astype(np.float32) # [0.].astype(np.float32)

scalar_vector_multiply[n,1](A,B,result)
print(result.item())

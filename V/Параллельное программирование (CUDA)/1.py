# 1. С использованием инструментария CUDA напишите программу, вычисляющую сумму двух произвольных векторов на GPU.

import numpy as np
from numba import vectorize

#UFUNC (самая быстрая)
@vectorize(['float32(float32, float32)'], target='cuda')
def vector_addition(a, b):
    return a + b

n = 1000000
a = np.random.randn(n).astype(np.float32)
b = np.random.randn(n).astype(np.float32)
# print(a)
# print(b)

result = vector_addition(a, b)
print(result)

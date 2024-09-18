# С использованием инструментария CUDA напишите программу, содержащую ошибку, связанную с вычислениями на GPU.
#  Программа должна вывести в терминал подробное сообщение об этой ошибке и попытаться её обработать.

#В Numba cuda нет встроенных обработчиков ошибок при вычислениях. Классы ошибок импортируются в основной модуль ошибок оболочки питона.
# print(cuda.cudadrv.error.__dict__)
# cuda.cuda_error тоже вызывает runtimeerror, она пустая

# Подробнее в 
# print(cuda.cudadrv.driver.__file__)

# print(cuda.CudaSupportError.__dict__) также только deadmemory, и остальные, но они бессмысленные, так как все ссылаются на runtimeerror, кроме ApiError
# print(cuda.__dict__)

import numpy as np
from numba import cuda

@cuda.jit
def matmul(A,B,C):
    i= cuda.grid(1)
    tmp=0.
    try:
        for k in range(len(A)+1):
            tmp+=A[i]*B[i]
        C[i]=tmp
    except Exception:
        tmp=0.
        for k in range(len(A)):
            tmp+= A[i]*B[i]
        C[i]=tmp
        print("Ошибка1")

n = 1024
A = np.random.randn(n).astype(np.float32)
B = np.random.randn(n).astype(np.float32)

result = np.zeros(n, dtype=np.float32)

try:

    matmul[n,1](A,B,result)

except Exception:

    print("Ошибка2")

print(result)

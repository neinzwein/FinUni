# 7. С использованием инструментария CUDA напишите программу, использующую встроенные средства профилирования. 
# В качестве примера для профилирования можно взять любую другую программу из пп. 1-6.

import numpy as np
from numba import vectorize
# from numba.cuda import profile_start,profile_stop
from numba.cuda import event_elapsed_time
from numba.cuda import event

# # # profiling() на входе и выходе
# # # #init
# # # if cuda.is_available():
# # #     pass

@vectorize(['float32(float32, float32)'], target='cuda')
def vector_addition(a, b):
    return a + b

n = 1000000
a = np.random.randn(n).astype(np.float32)
b = np.random.randn(n).astype(np.float32)
# print(a)
# print(b)

# profile_start() # штука для Nsight

s1 = event()
s2 = event()

s1.record()
result = vector_addition(a, b)
s2.record()

# profile_stop()

s2.synchronize()

print(event_elapsed_time(s1,s2))

print(result)


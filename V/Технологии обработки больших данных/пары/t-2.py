# 21
# numpy.asanyarray
import numpy as np

a = [1, 2]
print(type(a))
a = np.asanyarray(a)
print(type(a))

a = np.array([(1., 2), (3., 4)], dtype='f4,i4').view(np.recarray)
print(np.asanyarray(a) is a)
# Средствами numpy рассчитать произведения четных чисел от 2 до 20 на числа,
# которые больше их на единицу.

import numpy as np

array = np.arange(2,21)

# print(array[0:18:2])
# print(array[1:19:2])
print(array[0:18:2]*array[1:19:2])
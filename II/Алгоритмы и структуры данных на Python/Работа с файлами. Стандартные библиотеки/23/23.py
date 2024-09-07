# Создать матрицу 8 на 10 из случайных целых (используя модуль numpy.random)
# чисел из диапазона от 0 до 10 и найти в ней строку
# (ее индекс и вывести саму строку), в которой сумма значений минимальна.

import numpy as np

matrix = np.random.randint(low=0,high=10,size=(8,10))

# print(matrix)
# print(n.sum(matrix,axis=1))
# print(np.min(np.sum(matrix,axis=1)))

print("Index: "+str(np.sum(matrix,axis=1).argmin()))
print("String :"+str(matrix[np.sum(matrix,axis=1).argmin()]))
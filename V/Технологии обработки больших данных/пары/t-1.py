# Дервук Максим А. ЗБ-ПИ20-1


# Создать  массив `arr` размерности (10, 4) из случайных  целых чисел от 0 до 50.
#  Найти самое частое  число в массиве (вывести на экран его  значение и информацию о расположении 
#  всех этих значений в исходном массиве).  Вернуть массив (3, 4),
#  содержащий 3 строки  из исходного массива, в которых находится  наибольшее количество самых частотных  значений.э
#  Код должен корректно работать  в случае, если сразу несколько чисел  являются самыми частотными. Решить  задачу средствами numpy и/или pandas. 
# Не  использовать циклы и конструкции  стандартного Python там, где можно  использовать возможности данных  библиотек

# import pandas as pd
# import numpy as np

# arr = np.random.randint(low = 0,high = 51, size = (10,4))
# df = pd.DataFrame(arr)

# # print(df)
# #всех этих значений в исходном массиве
# common = df.stack().value_counts()
# # print(common)

# most_common = common[common == common.max()]
# # print(most_common)

# positions = df.isin(most_common.index)
# # print(positions)

# rows_count = positions.sum(axis=1)
# #ряды
# res_rows = df.loc[rows_count.nlargest(3).index]

# print(f"{rows_count},{res_rows}")

import pandas as pd
import numpy as np

arr = np.random.randint(low=0,high = 51, size = (10,4))
df = pd.DataFrame(arr)

print(df)

common = df.mode().value_counts()
print(common)
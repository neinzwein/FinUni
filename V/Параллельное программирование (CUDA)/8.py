# 8. С использованием инструментария CUDA напишите программу,
#  вычисляющую коэффициенты линейной регрессии для данных, 
# приведённых в таблице ниже:

string = """Ботсвана | 0.0676 | 0.1310
Камерун | 0.0458 | 0.0415
Эфиопия | 0.0094 | 0.0212
Индия | 0.0115 | 0.0278
Индонезия | 0.0345 | 0.0221
Кот-д’Ивуар | 0.0278 | 0.0243
Кения | 0.0146 | 0.0462
Мадагаскар | -0.0102 | 0.0219
Малави | 0.0153 | 0.0361
Мали | 0.0044 | 0.0433
Пакистан | 0.0295 | 0.0263
Танзания | 0.0184 | 0.0860
Таилан | 0.0341 | 0.0395"""

import re
import numpy as np
from numba import cuda

string = re.split(r' \| |\n',string)
# print(string)
string = np.array(string)
h = np.array(string[1::3]).astype(np.float32)
invest = np.array(string[2::3]).astype(np.float32)

@cuda.jit
def linear_regression_kernel(h, invest, coef, intercept):
    i = cuda.grid(1)
    if i == 0:
        n = len(h)
        sum_h = sum_h_i = sum_squared_h = sum_invest = 0.0
        for i in range(n):
            sum_h += h[i]
            sum_invest += invest[i]
            sum_h_i += h[i] * invest[i]
            sum_squared_h += h[i] * h[i]
        coef[0] = (n * sum_h_i - sum_h * sum_invest) / (n * sum_squared_h - sum_h * sum_h)
        intercept[0] = (sum_invest - coef[0] * sum_h) / n
coef = np.zeros(1, dtype=np.float32)
intercept = np.zeros(1, dtype=np.float32)

h_device = cuda.to_device(h)
invest_device = cuda.to_device(invest)
coef_device = cuda.to_device(coef)
intercept_device = cuda.to_device(intercept)

linear_regression_kernel[1, 1](h_device, invest_device, coef_device, intercept_device)
coef_device.copy_to_host(coef)
intercept_device.copy_to_host(intercept)
print("Коэффициент: ", coef[0])
print("Перехват: ", intercept[0])
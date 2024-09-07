# Напишите функцию, которая находит максимум функции f(x) в точках отрезка [a,b] с
# постоянным шагом h. Параметрами функции являются f, a, b, h. Параметры a, b, h – необязательные,
# по умолчанию a=0, b=1, h=0.1.
# Используя эту функцию, найдите максимум функции (6-x)sin(x/6) на отрезке [0, 12].

import math

def Function(f:str, a:float=0, b:float=1, h:float=0.1)->float:

    def main_function(x:float)->float:
        return (6 - x) * math.sin(x / 6)

    def drange(a:float=0,b:float=1,h:float=0.1)->iter:
        while a<b:
            yield float(a)
            a+=h

    def max_of_f(a:float=0,b:float=1,h:float=0.1)->float:
        max_value = main_function(a)
        for i in drange(a,b,h):
            max_value=max(max_value,main_function(i))
        return max_value

    return max_of_f(a,b,h)

print(Function("(6-x)*sin(x/6)",0,12,0.1))
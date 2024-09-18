# Вариант 4
#  Библиотека Dask (4+8)  (в работе… будут уточненич… 11.9)
# см.   TOBD_lec_07*
# Задание t-5  (см. пример в TOBD_lec_11_dask_v3.ipynb)
# Задать N1 задач, N2 функций, вычисляющих выражения от нескольких формальных параметров 
# построить граф зависимостей dsk с вершиной - одной из задач и визуализировать его. (граф расположить горизонтально)

# N1 = 8, N2=4:  t0 (t1,t2)  t2(t3)    t1(t5,t4)   t4(t6,t7)

import dask
# from dask.threaded import get
from dask.delayed import Delayed

#N1
def t0(t1,t2)->None:
    pass

def t1(t5,t4)->None:
    pass

def t2(t3)->None:
    pass

def t3()->None:
    pass

def t4(t6,t7)->None:
    pass

def t5()->None:
    pass

def t6()->None:
    pass

def t7()->None:
    pass

dsk = {
    't0': (t0, 't1', 't2'),
    't1': (t1, 't5', 't4'),
    't2': (t2, 't3'),
    't3': (t3,),
    't4': (t4, 't6', 't7'),
    't5': (t5,),
    't6': (t6,),
    't7': (t7,)
}

# print(get(dsk, 't0'))

delayed_dsk = Delayed("t0", dsk)
delayed_dsk.visualize(rankdir='LR')

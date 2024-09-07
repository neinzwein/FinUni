# При помощи функций map/filter/reduce превратить список целых чисел в строку,
# содержащую строковое представление этих чисел, разделенных пробелами.

list_int=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

#map
print(' '.join(map(str,list_int)))

#filter
def func():
    for i in range(0,len(list_int)):
        list_int[i]=str(list_int[i])

print(' '.join(filter(func(),list_int)))

#reduce
from functools import reduce
print(reduce(lambda x,y:str(x)+' '+str(y),list_int))
# Дан список из N чисел с плавающей точкой. Напишите функцию,возвращающую индексы
# списка в том порядке, в котором соответствующие им элементы образуют
# неубывающую последовательность. (Результат должен быть списком целых чисел)

from random import randint

def Function(N:int):

    l=[randint(0,10) for i in range(N)]
    indexes = [i for i in range(N)]

    # print(l,indexes)

    for i in range(N):
        for j in range(N):
            if l[i]<l[j]:
                l[i],l[j]=l[j],l[i]
                indexes[i],indexes[j]=indexes[j],indexes[i]

    # print(l,indexes)
    return indexes

print(f"{Function(N=randint(5,10))}")


# Сортировка слиянием (англ. merge sort) позволяет отсортировать данный массив при помощи O(nlogn)) сравнений элементов.

# Проще всего реализовать сортировку слиянием при помощи рекурсивной функции. Если длина данного массива равна 0 или 1, то массив уже отсортирован. 
# Иначе необходимо разделить этот массив на две части равной (или отличающейся на 1) длины, каждую из них отсортировать рекурсивно,
# затем слить результат двух полученных массивов в исходный массив.

# Реализуйте алгоритм сортировки слиянием. Решение оформите в виде функции merge_sort(a: list) -> list

from random import shuffle

def merge_sort(a:list)->list:

    if len(a)<=1:
        return a
    
    middle = len(a)//2
    left=[a[i] for i in range(0,middle)]
    right = [a[i] for i in range(middle,len(a))]
    
    merge_sort(left)
    merge_sort(right)

    c = merge(left,right)
    for i in range(len(a)):
        a[i]=c[i]

    return a

def merge(a:list,b:list)->list:

    c = [0] * (len(a)+len(b))
    
    i=k=n=0 #i-a b-k c-n

    while i<len(a) and k<len(b):
        if a[i]<b[k]:
            c[n]=a[i]
            i+=1
            n+=1
        else:
            c[n]=b[k]
            k+=1
            n+=1
    
    while i<len(a):
        c[n]=a[i]
        i+=1
        n+=1

    while k<len(b):
        c[n]=b[k]
        k+=1
        n+=1

    return c

a = list(range(1,20))
shuffle(a)

print(a)

merge_sort(a)

print(a)
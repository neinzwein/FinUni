# Даны два списка a и b упорядоченных по неубыванию. Объедините их в один упорядоченный список.

# Решение оформите в виде функции merge(a: list, b: list) -> list, возвращающей новый список и не модицифицирующей данные списки.

a = list(range(1,12,2))
b = list(range(0,10,2))

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


print(f"{merge(a,b)}")
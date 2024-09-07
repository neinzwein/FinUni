# Даны два списка чисел, упорядоченных по возрастанию (каждый список состоит из различных элементов).
# Найдите пересечение данных множеств, то есть те числа, которые входят в оба массива. Алгоритм должен иметь сложность O(n+m). 
# То есть, количество операций алгоритма должно быть не больше, чем заранее известная константа, умноженная на (n+m).

# Решение оформите в виде функции intersection(a: list, b: list) -> list, возвращающий пересечение двух данных списков. Полученный список должен быть упорядочен по возрастанию.

a = list(range(0,15,6))
b = list(range(0,15,3))

#set & set

# def intersection(a:list,b:list)->list:
#     return [value for value in a if value in b]

# print(f"{intersection(a,b)}")

def intersection(a:list,b:list)->list:
    i,j=0,0
    result=[]

    while i<len(a) and j<len(b):

        if a[i]<b[j]:
            i+=1

        elif a[i]>b[j]:
            j+=1

        else:
            result.append(a[i])
            i+=1
            j+=1
        
    return result

print(f"{intersection(a,b)}")
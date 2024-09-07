# Дана дробь 𝑛/𝑚 , n и m - натуральные числа. Напишите 2 функции, которые сокращают эту дробь, то есть находят числа p и q такие, что 𝑛/𝑚 = 𝑝/𝑞 , и дробь 𝑝/𝑞 — несократимая:

# • аргументами функции являются числа n, m, функция возвращает кортеж (p, q);

# • аргументом функции является список [n, m], функция не возвращает значения, а изменяет этот список на [p, q].

# Для поиска НОД воспользуйтесь функцией из Домашнего задания 2.

def Function(a,b):
    a,b = max(a,b),min(a,b)
    while b!=0: 
        a = b%a
        a,b = max(a,b),min(a,b)

    return a

def first(n, m)->set:
    nod = Function(n,m)
    p,q = n/nod,m/nod

    return (p,q)

def second(list_nm:list)->list:
    n,m = list_nm
    nod = Function(n,m)
    p,q = n/nod,m/nod

    list_nm=[p,q]

    return list_nm

print(f"{first(n=5,m=15)}")

print(f"{second(list_nm=[5,15])}")

# def Function1(n,m):
#     p,q=n,m
#     while (min(n,m)!=0):
#         if (n>m):
#             n=n%m
#         elif (m>n):
#             m=m%n
#     return p/max(n,m),q/max(n,m)

# print(Function1(21,14))

# def Function2(list_n):
#     p,q=list_n[0],list_n[1]
#     while (min(list_n[0],list_n[1])!=0):
#         if (list_n[0]>list_n[1]):
#             list_n[0]=list_n[0]%list_n[1]
#         elif (list_n[1]>list_n[0]):
#             list_n[1]=list_n[1]%list_n[0]
#     list_n[0],list_n[1]=p/max(list_n[0],list_n[1]),q/max(list_n[0],list_n[1])
#     return list_n

# print(Function2([14,21]))

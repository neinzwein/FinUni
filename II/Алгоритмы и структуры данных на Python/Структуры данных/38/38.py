# Имеется ряд словарей с пересекающимися ключами (значения - положительные числа). Напишите 2 функции, которые делают с массивом словарей следующие операции:
# 1-ая функция max_dct(dicts) формирует новый словарь по правилу:

# Если в исходных словарях есть повторяющиеся ключи, выбираем среди их значений максимальное и присваиваем этому ключу
# (например, в словаре_1 есть ключ “а” со значением 5, и в словаре_2 есть ключ “а”, но со значением 9.
# Выбираем максимальное значение, т. е. 9, и присваиваем ключу “а” в уже новом словаре).  

# Если ключ не повторяется, то он просто переносится со своим значением в новый словарь
# (например, ключ “с” встретился только у одного словаря, а у других его нет. Следовательно, переносим в новый словарь этот ключ вместе с его значением). 
# Сформированный словарь возвращаем.

# 2-ая функция sum_dct(dicts) суммирует значения повторяющихся ключей.
# Значения остальных ключей остаются исходными.
# (Проводятся операции по аналогу первой функции, но берутся не максимумы, а суммы значений одноименных ключей). Функция возвращает сформированный словарь.

def max_dct(*dicts:dict)->dict:
    res_dict={}
    for d in dicts:
        for k,v in d.items():
            if k not in res_dict:
                res_dict[k]=v
            elif k in res_dict and res_dict[k]<d[k]:
                res_dict[k] = v
    return res_dict

def sum_dct(*dicts:dict)->dict:
    res_dict={}
    for d in dicts:
        for k,v in d.items():
            if k not in res_dict:
                res_dict[k] = v
            elif k in res_dict:
                res_dict[k]+=v

    return res_dict

dict1 = {"a":5,"d":8}
dict2 = {"a":9,"b":4}
dict3 = {"a":3,"b":5,"c":6}

print(max_dct(dict1,dict2,dict3))
print(sum_dct(dict1,dict2,dict3))

# from collections import Counter
# from functools import reduce

# def sum_dct(*dicts:list[dict])->list[dict]:
#     return dict(reduce(lambda a,b : Counter(a) + Counter(b),dicts))

# def max_dct(*dicts:list[dict])->list[dict]:
#     return dict(reduce(lambda a,b : Counter(a) | Counter(b),dicts))

# print(max_dct(dict1,dict2,dict3))
# print(sum_dct(dict1,dict2,dict3))
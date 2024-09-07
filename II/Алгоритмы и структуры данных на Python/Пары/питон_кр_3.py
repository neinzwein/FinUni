list_of_dicts=[{"Одежда":"Майка","Цвет":"Белый","Цена":"1000"},
               {"Место":"Первое","Приз":"Золото","Имя":"Вася"},
               {"Месяц":"Сентябрь","Праздник":"День знаний","Год":"1999"}]

def number_3(list_of_dicts):
    all_dicts={}
    for dicts in list_of_dicts:
        all_dicts.update(dicts)
    return all_dicts

# print(number_3(list_of_dicts))

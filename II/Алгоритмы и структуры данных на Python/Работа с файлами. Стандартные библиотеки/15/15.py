# Создайте текстовый файл, содержащий информацию о товарах и ценах на них. Каждая строка файла имеет вид: АРТИКУЛ(число, обязательное поле), НАЗВАНИЕ ТОВАРА: ЦЕНА в рублях
# Используя данный файл:
# • найдите цену указанного товара по его названию, или выдайте сообщение о том, что цена не определена или такого товара нет;
# • найдите цену указанного товара по его артиклу, или выдайте сообщение о том, что цена не определена;
# • добавьте в файл информацию о трех новых товарах;
# • удалите из файла информацию о товаре по его названию;
# • создайте новый файл, в котором товары будут упорядочены в порядке возрастания цен. Выведите на экран информацию о трех самых дешевых и двух самых дорогих товарах.

# with open("example.txt","r+",encoding="utf-8") as f:
#     dict_list={}
#     for line in f.read().splitlines():
#         k,v = line.split(":")
#         dict_list[tuple(k.split(","))]=v

#     def FindByName(name):
#         if (str(dict_list.keys())).count(name)==0:
#             return "Такого товара нет"
#         for key,value in dict_list.items():
#             if name in key or name==key:
#                 if value.isdigit()==True:
#                     return value
#                 else:
#                     return "Цена не определена"
#                 #Функции одинаковы
#     # def FindByArticle(article):
#     #     if (str(dict_list.keys())).count(article)==0:
#     #         return "Такого товара нет"
#     #     for key,value in dict_list.items():
#     #         if article in key or article==key:
#     #             if value.isdigit()==True:
#     #                 return value
#     #             else:
#     #                 return "Цена не определена"

#     def addToFile(article,name,price):
#         line = article+","+name+":"+price+"\n"
#         with open("example.txt","a+",encoding="utf-8") as f:
#             dict_list[article,name]=price
#             f.writelines(line)

#     def eraseFromFile(name):
#         with open("example.txt","w+",encoding="utf-8") as f:
#             for line in dict_list.copy():
#                 if name in line:
#                     dict_list.pop(line)
#             for k,v in dict_list.items():
#                 f.writelines(str(k[0])+","+str(k[1])+":"+str(v)+"\n")

#     def SortByPrice():
#         with open("SortedPrices.txt","a+",encoding="utf-8") as f2:
#             sortRes=dict(sorted(dict_list.items(),key=lambda x:x[1]))
#             for k,v in sortRes.items():
#                 f2.write(str(k[0])+","+str(k[1])+":"+str(v)+"\n")

#     def firstLast():
#         with open("SortedPrices.txt","r+",encoding="utf-8") as f2:
#             reader=f2.readlines()
#             print(reader[0])
#             print(reader[1])
#             print(reader[2])
#             print(reader[-2])
#             print(reader[-1])

# # print(FindByName("Футболка"))
# # print(FindByName("Пиджак"))
# # print(FindByName("Свитер"))
# #
# # print(FindByName("00000001"))
# # print(FindByName("54678654"))

# # addToFile("12345678","Брюки","2000")
# # addToFile("87654321","Куртка","30000")
# # addToFile("12348765","Шапка","2400")

# # eraseFromFile("Брюки")
# # eraseFromFile("Шапка")

# # SortByPrice()

# # firstLast()

# # Для нормальной работы добавьте цены

# ______________________________

import pandas as pd


def check_fields(data:pd.DataFrame,col:str,param:str)->bool:

    try:

        if param not in data[col].values:
            print(f"Товара под {col} с названием {param} нет")
            raise Exception
        
        # print(data.loc[data[col]==param,"Цена"].values)

        if data.loc[data[col]==param,"Цена"].isna().item()==True:
            print(f"Нет цены у товара с {col} == {param}")
            raise Exception
        
        else:
             return True
        
    except Exception:
        return False

def getter(data:pd.DataFrame,col:str,param:str):
     
     if check_fields(data=data,col=col,param=param)==True:
        return data.loc[data[col]==param,"Цена"].values[0]

def setter(data:pd.DataFrame,article:str,name:str,price:str)->pd.DataFrame:

    data.loc[len(data)] = [article,name,price]

    return data

def remove(data:pd.DataFrame,name:str)->pd.DataFrame:

    # print(data.loc[data["Название"]==name].index[0])

    data.drop(index=data.loc[data["Название"]==name].index[0],inplace=True)

    return data

def sortPrice(data:pd.DataFrame):

    data.sort_values(by=['Цена'],inplace=True,na_position='first')

    print(data[data['Цена'].notna()].head(3))
    print(data[data['Цена'].notna()].tail(2))

    data.to_csv('sorted_list.txt',header=1,index=None,sep=',',mode='a')


data = pd.read_csv('example.txt', sep=",|:", header=0, engine='python', dtype=str)

# print(data)

# print(getter(data=data,col="Название",param="Футболка"))
# print(getter(data=data,col="Название",param="Пиджак"))
# print(getter(data=data,col="Название",param="Найкпро"))

# print(getter(data=data,col="Артикул",param="42112421"))
# print(getter(data=data,col="Артикул",param="00000021"))
# print(getter(data=data,col="Артикул",param="001321230021"))

setter(data=data,article='0034342525',name='Кандибобер',price='1199')
setter(data=data,article='0033245325',name='Колготки',price='1299')
setter(data=data,article='02535532525',name='Сандали',price='1399')

# print(data)

# remove(data=data,name='Кандибобер')

# print(data)

sortPrice(data=data)

# print(data)
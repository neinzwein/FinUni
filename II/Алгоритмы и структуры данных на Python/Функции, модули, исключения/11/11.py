# Создайте текстовый файл, содержащий информацию о товарах и ценах на них.
# Каждая строка файла имеет вид: НАЗВАНИЕ ТОВАРА: ЦЕНА.
# Используя данный файл добавьте в файл информацию о трех новых товарах таким образом, что:
# - Если в файле еще нет строки с таким названием, то новый товар добавляется
# - Если в файле уже есть строка с таким названием, то новая строка не добавляется,
# а в уже существующей строке изменяется цена

# def Function(file,key,value):
#     try:
#         dict_list={}
#         with open(file=file,mode="r+",encoding="utf-8") as f:
#             reader=f.read().splitlines()
#             for line in reader:
#                 k,v=line.split(":")
#                 dict_list[k]=v
#             dict_list[key]=value
#             f.seek(0)
#             for k,v in dict_list.items():
#                 f.write(f'{k}:{v}\n')
#     except FileNotFoundError:
#         print("Файла не существует")

# Function("Shops.txt","Дыня","100")
# Function("Shops.txt","Арбуз","50")

# поясню - ты добавляешь в файл эти 2 строчки, поэтому после запуска проги они будут уже в файле, удали их

# но эта версия открывает и закрывает каждый раз, так не пойдет

def get_kv(file)->dict:
    dict_list={}
    reader = file.read().splitlines()
    for line in reader:
        k,v = line.split(":")
        dict_list[k]=v
    return dict_list

def set_kv(key,value,dict_list)->dict:
    dict_list[key]=value
    return dict_list

f = open(file="Shops.txt", mode="r+",encoding="utf-8")
f.write("Апельсин:200\nОгурец:300\n")

dict_list = get_kv(file=f)
f.close()

set_kv(key="Дыня",value="100",dict_list=dict_list)
set_kv(key="Арбуз",value="50",dict_list=dict_list)

f = open(file="Shops.txt",mode="a",encoding="utf-8")
# f.seek(0)

for k,v in dict_list.items():
    f.write(f"{k}:{v}\n")

f.close()
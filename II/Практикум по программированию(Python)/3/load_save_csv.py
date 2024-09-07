import csv
def load_table_csv(f):
#f="Одежда.csv"
    startname,endname=f.split('.')
    if endname=="csv":
        with open(f, newline = '',encoding='utf-8') as csvfile:
            try:
                reader = csv.DictReader(csvfile,delimiter=";")
                rows= [r for r in reader]
                for item in rows:
                    for key,value in item.items():
                        if item[key]=='':
                            item[key]=None
                return rows
            except FileNotFoundError:
                print('Файл не найден')
def save_table_csv(f,rows):
    with open(f,'w',newline = '',encoding='utf-8') as csvfile:
        try:
            writer = csv.writer(csvfile,delimiter=';')
#Первую строку(заголовки)
            writer.writerow(rows[0].keys())
#Записываем строки в столбцы
            for dict_item in rows:
                writer.writerow(dict_item.values())
        except FileNotFoundError:
            print("Файл не найден")
rows=[{'Одежда': 'Галстук', 'Цвет': 'Бежевый', 'Цена': None}, {'Одежда': 'Трусы', 'Цвет': 'Красный', 'Цена': '100'}, {'Одежда': 'Майка', 'Цвет': 'Белый', 'Цена': None}, {'Одежда': 'Кепка', 'Цвет': None, 'Цена': None}]
save_table_csv('Одежда1.csv',rows)
f="Одежда.csv"
print(load_table_csv(f))

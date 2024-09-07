import pickle
#obj2=[{'Одежда': 'Пиджак', 'Цвет': 'Синий', 'Цена': '1500'},
#      {'Одежда': 'Галстук', 'Цвет': 'Красный', 'Цена': ''},
#      {'Одежда': 'Рубашка', 'Цвет': 'Белый', 'Цена': ''}]
def save_table_pkl(f,obj2):
    with open(f,"wb") as picklefile:
        try:
            reader = pickle.dump(obj2,picklefile)
        except FileNotFoundError:
            print('Файл не найден')
def load_table_pkl(f):
    with open(f,"rb") as picklefile:
        try:
            reader = pickle.load(picklefile)
            for row in reader:
                for value in row.values():
                    if value=='':
                        value=None
            return reader
        except FileNotFoundError:
            print('Файл не найден')

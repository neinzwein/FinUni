#f="Одежда.txt"
table=[]
def load_table_txt(f):
    startname,endname=f.split('.')
    if endname=="txt":
        with open(f,"r+",encoding="utf-8") as file:
            list_column=[]
            header = file.readline().split()
            reader = file.readlines()
            for rows in reader:
                rows = rows.replace("\n"," ")
                list_column.append(rows.split())
            for i in range(0,len(list_column)):
                dict_rows={}
#Вызываем ошибку, если строк в столбцах меньше, чем заголовков
                try:
                    for j in range(0,len(header)):
                        current_head=str(header[j])
                        dict_rows[current_head]=list_column[i][j]
                    table.append(dict_rows)
                except IndexError:
                    for j in range(0,len(header)):
                        current_head=str(header[j])
                        list_column[i].append(None)
                        dict_rows[header[j]]=list_column[i][j]
                    table.append(dict_rows)
#Проверка на None
            for item in table:
                for x,y in item.items():
                    if item[x]=='':
                        item[x]=None
            return table
#table=[{'Одежда': 'Футболка', 'Цвет': 'Черный', 'Цена': None},
#       {'Одежда': 'Штаны', 'Цвет': 'белый', 'Цена': '300'},
#       {'Одежда': 'Куртка', 'Цвет': 'синий', 'Цена': None},
#       {'Одежда': 'носки', 'Цвет': 'розовый', 'Цена': None}]
def save_table_txt(f):  
    startname,endname=f.split('.')
    if endname=="txt":
        with open(f,"w+",encoding='utf-8') as file:
            data=""
            data_list=[]
            count=0
            for dicts in table:
                header=[]
                body=[]
                for key,value in dicts.items():
                    if value == None:
                        value=''
                    header.append(key)
                    body.append(value)
                if count==0:
                    header = ' '.join(header)
                    header+='\n'
                    data_list.append(header)
                    count+=1
                body = ' '.join(body)
                body+='\n'
                data_list.append(body)
            reader = file.write(''.join(data_list))

table=[{'Одежда': 'Пиджак', 'Цвет': 'Синий', 'Цена': '1500'},
      {'Одежда': 'Галстук', 'Цвет': 'Красный', 'Цена': ''},
      {'Одежда': 'Рубашка', 'Цвет': 'Белый', 'Цена': ''}]
def get_rows_by_number(start,stop,table):
    current_data=[]
    stop+=1
    try:
        for i in range(start,len(table)):
            if start==stop:
                break
            start+=1
            current_data.append(table[i])
        return current_data
    except IndexError:
        print("Ошибка с индексами")
print(get_rows_by_number(0,1,table))
def get_rows_by_index(val,table):
    current_data=[]
#val=[0,2]
    try:
        for i in range(len(table)):
            if i in val:
                current_data.append(table[i])
        return current_data
    except IndexError:
        print("Слишком большое значение, введите меньше")
def get_column_types(by_number):
#by_number=1
    data_list=[]
    type_dict={}
    current=[]
    dict_data={}
    count=0
    for dicts in table:
        header=[]
        body=[]
        for key,value in dicts.items():
            if value=='':
                value=None
            header.append(key)
            body.append(value)
        if count==0:
            data_list.append(header)
            count+=1
        data_list.append(body)
    for i in range(0,len(data_list)):
        for j in range(0,len(data_list[i]),len(data_list[i])):
            current.append(data_list[i][by_number])
    for i in range(len(current)):
        dict_data[current[i]]=i
    for key,value in dict_data.items():
        if '.' in key:
            dict_data[key]=float
        elif key==True or key==False:
            dict_data[key]=bool
        try:
            if key==int(key):
                dict_data[key]=int
            else:
                dict_data[key]=str
        except ValueError:
            dict_data[key]=str
    return dict_data
def set_column_types(types_dict,by_number):
#by_number=1
#types_dict={int:int,str:str,float:float,bool:bool}
    data_list=[]
    current=[]
    count=0
    for dicts in table:
        header=[]
        body=[]
        for key,value in dicts.items():
            if value=='':
                value=None
            header.append(key)
            body.append(value)
        if count==0:
            data_list.append(header)
            count+=1
        data_list.append(body)
    for i in range(0,len(data_list)):
        for j in range(0,len(data_list[i]),len(data_list[i])):
            current.append(data_list[i][by_number])
    for i in range(len(current)):
        try:
            current[i]=list(types_dict.values())[i]
        except TypeError:
            print("Ты что-то напутал с типами")
    return current
#def get_values(column):
#def get_value(column):
#def set_values(values,column):
#def set_value(column):

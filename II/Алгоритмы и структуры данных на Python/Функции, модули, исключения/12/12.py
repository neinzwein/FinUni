# Даны файлы students.csv, results.csv, groups.csv, subjects.csv, teachers.csv. Разделены ";"
# Файл groups.csv имеет столбцы id, text_name, entry_year, где id - уникиальный идентификатор группы, text_name - наименование группы, entry_year - год поступления.
# students.csv имеет следующие столбцы: id, first_name, last_name, group_id, где id - уникальный идентификатор студента (номер зачетной книжки), first_name - Имя, last_name - фамилия, group_id - идентификатор группы, в которой он учится.
# result.csv имеет следующие столбцы: id - уникальный идентификатор записи, subject_id - идентификатор учебного предмета, student_id - уникальный идентификатор студента, att1 - результат первой аттестации, att2 - результат второй аттестации, exam - результат экзаменнационной или зачетной работы, total - общий результат, teacher_id - уникальный идентификатор преподавателя.
# subjects.csv имеет следующие столбцы: id - уникальный идентификатор предмета, subject_name - наименование предмета.
# teachers.csv: id - уникальный идентификатор преподавателя, first_name - Имя, last_name - фамилия, middle_name – отчество
# Надо написать функцию, которая принимает id преподавателя и id группы. Функция возвращает False, если данный преподаватель не преподавал у данной группы, None, если такого прподавателя не существует, иначе возвращается словарь, в котором ключами являются наименования предметов, а значениями словари, которые хранят в себе информации о количестве студентов, сдавших на 5, 4, 3 и 2 по данному предмету.
# 

import pandas as pd

def Function(teacher_id=0,group_id=0):

    # Проверка на существование препода
    with open(file='teachers.csv',mode='r',encoding='utf-8',newline='') as tf:
        df=pd.read_csv(tf,delimiter=';')
        if (teacher_id in df['id'].unique()) is False:
            print('Такого не существует')
            return None

    # Выборка студентов по условию (ищем) Получаем список группы
    with open(file='students.csv',mode='r',encoding='utf-8',newline='') as stf:
        df = pd.read_csv(stf,delimiter=';')
        newd=list(df['id'][df['group_id']==group_id])

    #Предмет - id
    with open(file='subjects.csv',mode='r',encoding='utf-8',newline='') as subf:
        df = pd.read_csv(subf,delimiter=';')
        data=df

    #Проверяем на то вел ли у группы / возвращаем нужный словарь (взята система оценивания ФУ)
    with open(file='result.csv', mode='r', encoding='utf-8', newline='') as rf:
        df = pd.read_csv(rf, delimiter=';')
        df = df.loc[:,['subject_id','student_id','total']][df['teacher_id']==teacher_id]

        # Проверка на ведение группы
        if (df.loc[df['student_id'].isin(newd)]).empty is True:
            return False
        else:
            df=df.loc[df['student_id'].isin(newd)]

            # Меняем стобальную систему оценок на пятибальную
            df.loc[df['total'] <= 50,'total'] = 2
            df.loc[(df['total'] >= 51) & (df['total']<=69), 'total'] = 3
            df.loc[(df['total'] >= 70) & (df['total']<=85), 'total'] = 4
            df.loc[(df['total'] >= 86) & (df['total']<=100), 'total'] = 5

            # # Подчищаем словарь предметов (Не обязательно)
            # for key,value in list(data.to_dict().items()):
            #     if (data.to_dict()[key] not in df['subject_id'].unique().tolist()):
            #         del data.to_dict()[key]

            # Кидаем название предметов по соответствию номеров предметов
            df = df.merge(data, left_on='subject_id', right_on='id', how='inner', right_index=False)
            df = df.loc[:,['subject_name','student_id','total']]

            #Создаём словарь словарей (Мдааа...Короче, меченый...)
            return {k : g['total'].value_counts().to_dict() for k, g in df.groupby(df['subject_name'])}


Function(0,0)
print(Function(1,21))
print(Function(1,1))
#  Создайте класс Ведомость, имеющий атрибут класса: список_дисциплин (значением является список с названиями дисциплин); 
# дисциплина (при задании значения проверять наличие дисциплины в атрибуте список_дисциплин), группа; 
# методы: put – добавляет в ведомость информацию об оценке студента (фамилия, оценка – параметры метода). 
# Для хранения данных внутри класса используйте словарь, в котором ключом является фамилия студента. 

# Возможные оценки – «отлично», «хорошо», «удовл.», «неудовл.», «н/я»; get – возвращает оценку, полученную студентом (фамилия студента – параметр метода);
# change – изменяет оценку, полученную студентом (фамилия студента и новая оценка – параметры метода);
# del – удаляет информацию о студенте из ведомости (фамилия студента – параметр метода); 
# result – возвращает кортеж из 5 чисел (количество каждого вида оценок в ведомости);
# __init__ – конструктор; __str__ – возвращает строку, содержащую заголовки (название экзамена, группа) и результаты экзамена в виде таблицы;
# count – возвращает количество студентов в ведомости; names – возвращает список фамилий, имеющихся в ведомости.
# Продемонстрируйте работу с классами, создав необходимые объекты и вызвав все их методы.

# Формулировка плохая ==> представляет собой только одну оценку на студента.

class Statement(object):
 
    possible_marks = list()

    data_marks={}

    def __init__(self,subjects:list,subject:str,group:str) -> None:
        
        #при задании значения проверять наличие дисциплины в атрибуте список_дисциплин
        if subject not in subjects:
            print(f"Предмета ""{subject}"" нет в {subjects}")
        else:
            self.subjects = subjects
            self.subject = subject
            self.group = group

    # put – добавляет в ведомость информацию об оценке студента (фамилия, оценка – параметры метода)
    def put(self,LastName:str,mark:str)->None:
        
        if mark not in self.possible_marks:
            print(f"Оценки {mark} не существует.\nСписок доступных оценок : {self.possible_marks}")
        else:
            self.data_marks[LastName] = mark
            # if LastName in self.data_marks.keys():
            #     self.data_marks[LastName].append(mark)
            # else:
            #     self.data_marks[LastName] = [mark]

    # get – возвращает оценку, полученную студентом (фамилия студента – параметр метода)
    def get(self,LastName:str)->str:
        
        if LastName not in self.data_marks.keys():
            return f"Студент с фамилией {LastName} не найден."
        else:
            return self.data_marks[LastName]

    # change – изменяет оценку, полученную студентом (фамилия студента и новая оценка – параметры метода);
    def change(self,LastName:str,mark:str)->None:
        
        if LastName not in self.data_marks.keys():
            print(f"Студент с фамилией {LastName} не найден.")
        elif mark not in self.possible_marks:
            print(f"Оценки {mark} не существует.\nСписок доступных оценок : {self.possible_marks}")
        else:
            self.data_marks[LastName] = mark

    # del – удаляет информацию о студенте из ведомости (фамилия студента – параметр метода)
    def delete(self,LastName:str)->None:
        self.data_marks.pop(LastName)


    #result – возвращает кортеж из 5 чисел (количество каждого вида оценок в ведомости);
    def result(self)->tuple:

        # src=list(self.data_marks.values())
        # return ( src.count("отлично"), src.count("хорошо"), src.count("удовл."), src.count("неудовл."), src.count("н/я"))

        count_marks = {c:0 for c in self.possible_marks}
        for v in self.data_marks.values():
            if v in count_marks:
                count_marks[v] +=1
        
        return tuple(count_marks.values())
        

    # __str__ – возвращает строку, содержащую заголовки (название экзамена, группа) и результаты экзамена в виде таблицы;
    def __str__(self) -> str:
        result = f"Название экзамена : {self.subject}\nгруппа : {self.group}\n"
        result+=f"Фамилия\t\t|\tОценка\n"
        for k,v in self.data_marks.items():
            result+= f"{k}\t|\t{v}\n"
        return result

    # count – возвращает количество студентов в ведомости
    def count(self)->int:
        return len(self.data_marks.keys())
    
    #names – возвращает список фамилий, имеющихся в ведомости.
    def names(self)->list:
        return list(self.data_marks.keys())
    
############################################################

if __name__ == '__main__':
    
    ListOfSubjects= ["Английский язык","Философия","Математика","История","Физкультура","Русский язык","Литература","Физика","Химия"]

    statement = Statement(subjects=ListOfSubjects,subject="Философия",group="ПИ")

    statement.possible_marks = ["отлично", "хорошо", "удовл.", "неудовл.", "н/я"]

    statement.put("Фамилия1","отлично")
    statement.put("Фамилия6","отлично")
    statement.put("Фамилия2","хорошо")
    statement.put("Фамилия3","удовл.")
    statement.put("Фамилия4","неудовл.")
    statement.put("Фамилия5","н/я")

    print(statement)

    # print(statement.get("Фамилия6"))

    # statement.change(LastName="Фамилия6",mark="хорошо")
    # print(statement.get("Фамилия6"))

    # statement.put("Фамилия7","отлично")
    # print(statement.get("Фамилия7"))
    # statement.delete(LastName="Фамилия7")
    # print(statement.get("Фамилия7"))

    # print(statement.result())

    # print(statement.count())

    # print(statement.names())
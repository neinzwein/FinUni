# Используя класс People в качестве базового, создайте класс-наследник Сотрудник (Worker), имеющий атрибуты: должность (post); 
# зарплата (salary) и методы: __init__ – конструктор; __str__ – для вывода строковой информации. 
# Создать два метода для класса Сотрудник и один метод для класса People.
# Используя класс Сотрудник в качестве базового создайте класс-наследник Преподаватель (Teacher), имеющий:
# атрибут дисциплины (disciplines), в котором хранятся названия дисциплин, которые ведет преподаватель; 
# методы __init__ и __str__;методы добавить_дисциплину (add_dis) и удалить_дисциплину (delete_dis), которые позволяют изменять список дисциплин. 
# Продемонстрируйте работу с классами, создав необходимые объекты и вызвав все их методы.

class People(object):
    
    def __init__(self,gender:chr) -> None:
        
        self.gender=gender

    def __str__(self) -> str:
        
        return f"{self.gender}"
    
    def change_Gender(self,gender)->None:
        
        self.gender = gender
    
class Worker(People):
    
    def __init__(self,gender:chr,post:str,salary:int) -> None:

        super(Worker, self).__init__(gender)

        self.post = post
        self.salary = salary

    def __str__(self) -> str:

       return f"Пол : {self.gender}\nДолжность : {self.post}\nЗарплата : {self.salary}"
    
    def change_post(self,post)-> None:

        self.post = post

    def change_salary(self,salary)->None:

        self.salary = salary

class Teacher(Worker):

    def __init__(self, gender:chr,post:str,salary:int,disciplines:list) -> None:

        super(Teacher,self).__init__(gender,post,salary)

        self.disciplines=[disciplines]

    def __str__(self) -> str:
        return f"Пол : {self.gender}\nДолжность : {self.post}\nЗарплата : {self.salary}\nДисциплины : {self.disciplines}"
    
    def add_dis(self,discipline):
        self.disciplines.append(discipline)

    def delete_dis(self,discipline):
        self.disciplines.remove(discipline)



if __name__=="__main__":
    
    p=People("М")
    print(p.gender)
    p.change_Gender("Ж")
    print(p.gender)

    w1=Worker(p,"Учитель",100000)

    t1=Teacher(w1.gender,"Учительница",w1.salary,"Английский язык")

    print(t1.gender)
    print(t1.post)
    print(t1.salary)
    print(t1.disciplines)

    t1.change_salary(120000)
    print(t1.salary)
    t1.add_dis("Психология")
    print(t1.__str__())
    t1.delete_dis("Английский язык")
    print(t1.__str__())
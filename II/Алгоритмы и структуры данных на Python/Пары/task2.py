#Задача (20 баллов)
#Написать функцию, которая находит корни квадратного уравнения по значениям его коэффициентов a, b и c.
#В случае, если корней нет, функция должна генерировать исключение. Если корни есть,
#- то возвращать список из двух корней (вещественных чисел). Если корень один, то в списке должно быть два
#одинаковых элемента. Составить пример вызова функции для конкретных параметров.
import math
def task2(*args):
    try:
        if len(args)==3:
            a,b,c=args
        else:
            raise Exception
    except Exception:
        return 'Количество переменных должно быть равно трём.'
    try:
#Неполные квадратные уравнения
        if a==0 and b!=0 and c!=0:
            x1=0
            x2=0
            return [x1,x2]
        if b==0 and c==0 and a!=0:
            x1=0
            x2=0
            return [x1,x2]
        if c==0 and a!=0 and b!=0:
            x1=0
            x2=-b/a
            return [x1,x2]
        if b==0 and a!=0 and c!=0:
            if -c/a >0:
                x1=math.sqrt(-c)/math.sqrt(a)
                x2=-(math.sqrt(-c)/math.sqrt(a))
                return [x1,x2]
            elif -c/a<0:
                raise Exception
#Полные квадратные уравнения
        if a!=0 and b!=0 and c!=0:
            D=math.pow(b,2)-(4*a*c)
            if D>0:
                x1=(-b+math.sqrt(D))/(2*a)
                x2=(-b-math.sqrt(D))/(2*a)
                x1,x2=float(x1),float(x2)
                return [x1,x2]
            elif D==0:
#По определению и по формуле может быть только 1 корень, но вы говорили, что делать так:
                x1 = (-b + math.sqrt(D)) / (2 * a)
                x2 = (-b - math.sqrt(D)) / (2 * a)
                x1, x2 = float(x1), float(x2)
                return [x1,x2]
            else:
                raise Exception
    except Exception:
        return 'Нет решений.'

#Полные квадратные уравнения
print(task2(3,-14,-5))
print(task2(5,-3,-2))
#Неполные квадратные уравнения
print(task2(-3,0,75)) #b=0
print(task2(6,3,0)) #c=0
print(task2(0,6,9)) #a=0
#Ошибка при введении чисел
print(task2(0))
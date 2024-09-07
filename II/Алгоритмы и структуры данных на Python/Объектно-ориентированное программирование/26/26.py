# Создайте класс Point (точка), у которого имеются 2 атрибута x и y (координаты) и методы __init__() и __str__(), и класс Treyg (треугольник),
# у которого есть: • три атрибута (верхушки треугольника). Значениями атрибутов являются объекты класса Point;
# • методы __init__() и __str__(); • метод sides(), возвращающий длины сторон треугольника; • метод perim(), вычисляющий периметр треугольника.
# Продемонстрируйте работу с классами, создав необходимые объекты и вызвав все их методы.

from math import pow,sqrt

class Point(object):

    def __init__(self,x,y) -> None:
        
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        
        return f"{self.x},{self.y}"
    
class Treyg(object):

    def __init__(self,a,b,c) -> None:
        
        self.a=a
        self.b=b
        self.c=c

    def __str__(self) -> str:

        return f"{self.a},{self.b},{self.c}"
    
    def sides(self):
        # По формуле гипотенузы (модуль разницы между а и б в квадрате) на модуль след точки
        AB=pow(abs(self.a.x-self.b.x),2)+pow(abs(self.a.y-self.b.y),2)
        BC=pow(abs(self.b.x-self.c.x),2)+pow(abs(self.b.y-self.c.y),2)
        CA=pow(abs(self.c.x-self.a.x),2)+pow(abs(self.c.y-self.a.y),2)
        return sqrt(AB),sqrt(BC),sqrt(CA)

    def perim(self): 
        return f"Периметр треугольника равен = {sum(self.sides())}"
    

point1=Point(0,0)
point2=Point(3,4)
point3=Point(6,0)

Triangle = Treyg(point1,point2,point3)

print("Стороны треугольника : ",Triangle.sides())
print(Triangle.perim())
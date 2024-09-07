# Создайте класс Point (точка), у которого имеются 2 атрибута x и y (координаты) и методы __init__() и __str__(), и класс Rect (прямоугольник), 
# у которого есть: • два атрибута (верхний левый угол и правый нижний угол прямоугольника). Значениями атрибутов являются объекты класса Point; 
# • методы __init__() и __str__(); метод sides(), возвращающий длины сторон прямоугольника; метод perim(), вычисляющий периметр прямоугольника.
# Продемонстрируйте работу с классами, создав необходимые объекты и вызвав все их методы.

#Класс точек
class Point(object):

    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"{self.x},{self.y}"

class Rect(object):

    def __init__(self,left,right) -> None:
        self.left = left
        self.right = right
    
    def __str__(self) -> str:
        return f"Прямоугольник с верхним левым углом - {self.left}\nС правым нижним углом{self.right}"
    
    def sides(self):
        w = abs(self.left.x-self.right.x)
        h = abs(self.left.y - self.right.y)
        return w,h

    def perim(self):
        w,h = self.sides()
        return 2*(w+h)

# 1 и 2 координаты
a=Point(0,0)
b=Point(10,5)

# Прямоугольник
r = Rect(a,b)

print("Стороны = ",r.sides())
print("Периметр = ",r.perim())
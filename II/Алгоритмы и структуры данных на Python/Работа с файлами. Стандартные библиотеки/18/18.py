# Из модулей math и numpy извлечь функции переводящие градусы в радианы. Соответственно извлеченным
# функциям перевести градусы в радианы двумя способами:
#
# перевести 75 градусов в радианы;
# перевести 180 градусов в радианы;
# перевести 90 градусов в радианы.
# Сравнить полученные два значения, переведенные из градусов в радианы между собой. Вывести результат
# в виде полученных значений в радианах и утверждение о равенстве или неравенстве полученных значений при
# переводе градусов в радианы разными способами.

from math import radians as r1

a1,b1,c1=r1(75),r1(180),r1(90)

from numpy import radians as r2

a2,b2,c2=r2(75),r2(180),r2(90)

if [a1,b1,c1] == [a2,b2,c2]:
    print("Равенство")
else:
    print("Неравенство")

print("math: "+a1.__str__(),b1.__str__(),c1.__str__())
print("numpy: "+a2.__str__(),b2.__str__(),c2.__str__())
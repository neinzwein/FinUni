# Создайте собственный модуль, поместив в него ваши функции,
# созданные в предыдущих заданиях.
# Напишите любую программу с использованием функций этого модуля.

from module.first import Function as Func1

print(f"{Func1(a=1,b=2,operation="+")}")
print(f"{Func1(a=3,b=2,operation="-")}")

from module.second import Function as Func2

print(Func2(3,15))

from module.third import Function,first,second as Func3,first,second

print(f"{first(n=5,m=15)}")
print(f"{second(list_nm=[5,15])}")
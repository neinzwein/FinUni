# Напишите функцию, имеющую 3 параметра: первые 2 - числа, третий - операция,
# которая должна быть произведена над ними. Если третий параметр «+», то нужно сложить числа,
# если «-» — вычесть, «*» — умножить, «/» — разделить (первое на второе).
# Функция возвращает результат выполнения операции над числами. Если операция не совпадает с указанными выше,
# то выводится сообщение "Неизвестная операция",и возвращается значение None.

def Function(a,b,operation):
    try:
        if (operation=="+"):
            return a+b
        elif (operation=="-"):
            return a-b
        elif (operation=="*"):
            return a*b
        elif (operation=="/"):
            return a/b
        else:
            raise ValueError
    except ValueError:
        print("Неизвестная операция")
        return None

print(Function(1,2,"+"))
print(Function(2,1,"-"))
print(Function(2,2,"*"))
print(Function(4,2,"/"))
print(Function(1,2,"++"))

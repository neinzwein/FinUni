# Напишите функцию, имеющую 3 параметра: первые 2 - числа, третий - операция, которая должна быть произведена над ними.
# Если третий параметр «+», то нужно сложить числа, если «-» — вычесть, «*» — умножить, «/» — разделить (первое на второе).
# Функция возвращает результат выполнения операции над числами. Если операция не совпадает с указанными выше, 
# то выводится сообщение "Неизвестная операция", и возвращается значение None.

def Function(a=0, b=0, operation:str=""): 
    if operation == "+":
        return a+b
    elif operation == "-":
        return a-b
    elif operation == "*":
        return a*b
    elif operation == "/":
        return a/b
    else:
        print("Незивестная операция")
        return None
    
print(f"{Function(a=1,b=2,operation="+")}")
print(f"{Function(a=3,b=2,operation="-")}")
print(f"{Function(a=2,b=2,operation="*")}")
print(f"{Function(a=2,b=2,operation="/")}")
print(f"{Function(a=1,b=2,operation="++")}")

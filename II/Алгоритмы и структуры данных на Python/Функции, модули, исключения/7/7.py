# Напишите функцию умножения неограниченного количества чисел.
# Если аргумент не является числом, то должна вызываться ошибка ValueError

def Function(*args):
    res = 1
    try:
        for number in args:
            # if str(number).isdigit()==False:
            #     raise ValueError
            res*=float(number)
    except ValueError:
        print(f"Задано не число == {number}")
    finally:
        return res

print(f"{Function(1,2,3,4,5,6)}")
print(f"{Function(1,2,3,4,"b",5,6)}")
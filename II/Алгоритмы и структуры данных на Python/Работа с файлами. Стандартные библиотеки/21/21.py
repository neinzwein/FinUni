# Создайте класс Заказ(Order), у которого есть атрибуты код_товара(code), цена(price),
# количество(count) и методы init и str. Создайте 2 класса-потомка: Опт(Opt) и Розница(Retail).
# В этих классах создайте методы init, str и сумма_заказа(summa), позволяющий узнать стоимость
# заказа. Для опта стоимость единицы товара составляет 95% от цены, а при покупке более 500
# штук – 90% цены. В розницустоимость единицы товара составляет 100% цены.
# Стоимость заказа равна произведению цены на количество.
# Продемонстрируйте работу с классами, создав необходимые объекты и методам.

class Order(object):

    def __init__(self,code,price,count) -> None:
        self.code = code
        self.price = price
        self.count = count

    def __str__(self) -> None:
        return f"Код товара : {self.code}\nЦена : {self.price}\nКоличество : {self.count}"
    
class Opt(Order):
    
    def __init__(self, code, price, count) -> None:
        super().__init__(code, price, count)

    def __str__(self) -> None:
        print("Opt")
        super().__str__()
        return f"{super().__str__()}\nСумма : {self.summa()}"
    
    def summa(self):
        
        if self.count<=500:
            discount = 0.95
            return self.price*self.count*discount
        
        elif self.count>500:
            discount = 0.9
            return self.price*self.count*discount

class Retail(Order):
    
    def __init__(self, code, price, count) -> None:
        super().__init__(code, price, count)

    def __str__(self) -> None:
        print("Retail")
        return f"{super().__str__()}\nСумма : {self.summa()}"
    
    def summa(self)-> None:
        discount = 1
        return self.price*self.count*discount
    
a=Opt(code=1234,price=1000,count=499)
b=Opt(code=1234,price=1000,count=500)

c=Retail(code=1234,price=1000,count=500)

print(a)
# print(a.summa())
print(b)
# print(b.summa())

print(c)
# print(c.summa())
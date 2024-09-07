# Создайте класс Заказ(Order), у которого есть атрибуты код_товара(code), цена(price),
# количество(count) и методы init и str. Создайте 2 класса-потомка: Опт(Opt) и Розница(Retail).
# В этих классах создайте методы init, str и сумма_заказа(summa), позволяющий узнать стоимость
# заказа. Для опта стоимость единицы товара составляет 95% от цены, а при покупке более 500
# штук – 90% цены. В розницустоимость единицы товара составляет 100% цены.
# Стоимость заказа равна произведению цены на количество.
# Продемонстрируйте работу с классами, создав необходимые объекты и методам.

class Order(object):

    discount = 1.0
    total = 0

    def __init__(self,code:int,price:int,count:int) -> None:

        self.code = code
        self.price = price
        self.count = count

    def __str__(self) -> str:
        return f"{self.code},{self.price},{self.count}"
    
class Opt(Order):

    def __init__(self, code:int, price:int, count:int) -> None:
        super(Opt,self).__init__(code, price, count)
    
    def __str__(self) -> str:
        return f"Опт {super(Opt,self).__str__()}"
        # return f"ОПТ\nЦена товара : {self.price}\nКоличество : {self.count}"
    
    def get_discount(self)->None:
        if self.count<=500:
            self.discount=0.95
        else:
            self.discount=0.90

    def summa(self)->float:
        self.get_discount()
        return (self.count*self.price)*self.discount

class Retail(Order):
    
    def __init__(self, code, price, count) -> None:
        super().__init__(code, price, count)

    def __str__(self) -> str:
        return f"Розница {super().__str__()}"
        # return f"ОПТ\nЦена товара : {self.price}\nКоличество : {self.count}"
    
    # def get_discount(self) -> None:
    #     return self.get_discount
    
    def summa(self)->float:
        # self.get_discount()
        return (self.count*self.price)*self.discount

if __name__ == "__main__":

    opt1 = Opt(1234,1000,500)
    opt2 = Opt(1234,1000,501)

    retail = Retail(1234,1000,500)

    # print(opt1)
    opt1.get_discount
    print(f"Сумма заказа : {opt1.summa()}")

    # print(opt2)
    opt2.get_discount
    print(f"Сумма заказа : {opt2.summa()}")

    # print(retail)
    # # retail.get_discount
    print(f"Сумма заказа : {retail.summa()}")


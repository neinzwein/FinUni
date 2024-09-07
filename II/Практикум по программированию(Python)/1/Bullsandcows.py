# 1.	Реализовать программу, с которой можно играть в логическую игру «Быки и коровы»
# (описание правил игры: http://робомозг.рф/Articles/BullsAndCowsRules ).
# Программа загадывает число, пользователь вводит очередной вариант отгадываемого числа,
# программа возвращает количество быков и коров и в случае выигрыша игрока сообщает о победе
# и завершается. Сама программа НЕ ходит, т.е. не пытается отгадать число загаданное игроком.
# Взаимодействие с программой производится через консоль, при запросе данных от пользователя
# программа сообщает, что ожидает от пользователя и проверяет корректность ввода.
from random import randint
class Place(object):

    def __init__(self,number):
        self.positions = list(map(int,str(number)))

    def __str__(self):
        return f"Заданое число : {self.positions}\nCows : {self.cows}\nBulls : {self.bulls}"

    def checkForNumber(self,number):
        if str(number).isdigit() == False or len(number) != 4:
            raise ValueError(f"Введёное значение неверно {number}")

    #Число отгаданных цифр не на своих местах
    def cows(self,number):
        arr = list(map(int,str(number)))
        return len([i for i in arr if i in self.positions])

    # #Число отгаданных цифр на своих местах
    def bulls(self,number):
        arr = list(map(int,str(number)))
        return len([i for i in arr if i in self.positions and arr.index(i)==self.positions.index(i)])

    def bullsAndCows(self,number):
        self.checkForNumber(number)
        cows=self.cows(number)
        bulls=self.bulls(number)
        print(f"Cows : {cows}\nBulls : {bulls}")
        if bulls==4:
            print("Победа")
            return False


a=Place(randint(1000,9999))
# print(a.positions)
result = True
while result != False:
    print("Ожидание хода игрока")
    result = a.bullsAndCows(input())
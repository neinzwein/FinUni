# 9.	(*) Реализовать программу, с которой можно играть в игру «Морской бой».
# Программа автоматически случайно расставляет на поле размером 10 на 10 клеток:
# 4 1-палубных корабля, 3 2-палубных корабля, 2 3-палубных корабля и 1 4-х палубный.
# Между любыми двумя кораблями по горизонтали и вертикали должна быть как минимум
# 1 незанятая клетка. Программа позволяет игроку ходить, производя выстрелы.
# Сама программа НЕ ходит т.е. не пытается топить корабли расставленные игроком.
# Взаимодействие с программой производится через консоль. Игровое поле изображается в виде
# 10 текстовых строк и перерисовывается при каждом изменении состояния поля. При запросе
# данных от пользователя программа сообщает, что ожидает от пользователя (в частности,
# координаты очередного «выстрела») и проверяет корректность ввода. Программа должна уметь
# автоматически определять потопление корабля и окончание партии и сообщать об этих событиях.

class Ship(object):

    def __init__(self,size,quantity):
        self.size=size
        self.quantity=quantity
        self.condition=[None,"X"]
        self.ship = [self.condition[0] for i in range(self.size)]

class Board(object):

    def __init__(self):
        self.board = [[" " for i in range(10)]for j in range(10)]

class Player(object):

    def __init__(self,player):
        self.player=player
        self.ships=[Ship(1,4),Ship(2,3),Ship(3,2),Ship(4,1)]

class SEUUBOY(object):

    def __init__(self):
        self.players=[Player(1),Player(2)]
        self.player = self.players[0]

    def switch(self):
        if self.player == self.players[0]:
            self.player = self.players[1]
        elif self.player == self.players[1]:
            self.player = self.players[0]
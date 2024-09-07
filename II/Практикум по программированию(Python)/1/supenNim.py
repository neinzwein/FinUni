# 3.	Реализовать программу, при помощи которой 2 игрока могут играть в игру «Супер ним».
# Правила игры следующие. На шахматной доске в некоторых клетках случайно разбросаны фишки
# или пуговицы. Игроки ходят по очереди. За один ход можно снять все фишки с какой-либо
# горизонтали или вертикали, на которой они есть. Выигрывает тот, кто заберет последние фишки.
# (описание правил игры: https://www.iqfun.ru/articles/super-nim.shtml )
# Взаимодействие с программой производится через консоль. Игровое поле изображается в виде
# текстовых строк и перерисовывается при каждом изменении состояния поля. При запросе данных
# от пользователя программа сообщает, что ожидает от пользователя (в частности, координаты
# новой отметки на поле) и проверяет корректность ввода. Программа должна уметь автоматически
# определять, что партия окончена, и сообщать о победе одного из игроков. Сама программа НЕ
# ходит, т.е. не пытается выбирать строки или столбцы с целью победить в игре.

from random import choices

class Player(object):

    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    dig = ['8', '7', '6', '5', '4', '3', '2', '1']

    def __init__(self,player):
        self.player = player
        self.x1, self.y1, self.x2, self.y2 = '', '', '', ''
        self.z = ''

    def __str__(self):
        return f"{self.x1},{self.y1},{self.x2},{self.y2},{self.z}"

    def check_first(self, xy):
        try:
            xy = xy.lower().split()
            if len(xy) != 2:
                raise Exception
            if (any([elem in xy for elem in self.abc]) == False or
                    any([str(elem) in xy for elem in range(1,9)]) == False):
                raise Exception
            return xy
        except Exception:
            while True:
                print("Некорректные данные. Доступные данные : ", self.abc, [str(i) for i in range(1, 9)])
                xy=input("Введите координаты : ").lower().split()
                if len(xy) == 2:
                    if (any([elem in xy for elem in self.abc]) == True and
                            any([str(elem) in xy for elem in range(1, 9)]) == True):
                        return xy

    def decode_first(self, xy):
        x, y = xy
        if x in self.abc:
            x, y, z = [i == int(y) for i in range(8, 0, -1)].index(True), self.abc.index(x), "vertical"
        else:
            x, y, z = [i == int(x) for i in range(8, 0, -1)].index(True), self.abc.index(y), "horizontal"
        self.x1, self.y1, self.z = x, y, z
        return self.x1, self.y1, self.z

    def check_second(self, xy, z):
        try:
            xy = xy.lower()
            if z == "vertical" and xy in self.abc:
                raise Exception
            elif z == "horizontal" and any([str(elem) == xy for elem in range(1, 9)]) == True:
                raise Exception
            if len(xy) != 1:
                raise Exception
            if xy not in self.abc and any([str(elem) == xy for elem in range(1, 9)]) == False:
                raise Exception
            return xy
        except Exception:
            while True:
                if z == "vertical":
                    print("Некорректные данные. Доступные данные : ", [i for i in range(1, 9)])
                    xy = input("Введите координату : ").lower()
                    if len(xy) == 1:
                        if any([str(elem) == xy for elem in range(1, 9)]) == True:
                            return xy
                elif z == "horizontal":
                    print("Некорректные данные. Доступные данные : ", self.abc)
                    xy = input("Введите координату : ").lower()
                    if len(xy) == 1:
                        if xy in self.abc:
                            return xy

    def decode_second(self, xy):
        if xy in self.abc:
            self.x2, self.y2 = self.x1, self.abc.index(xy)
        else:
            self.x2, self.y2 = [i == int(xy) for i in range(8, 0, -1)].index(True), self.y1
        return self.x2, self.y2

class Board(object):

    def __init__(self):
        self.board = [choices([" ", "*"], k=8) for i in range(8)]

    def __str__(self):
        abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        show = ["   "+"___ "*8]
        for i in range(len(self.board)):
            show.append(f"{len(self.board)-i}\t"+' | '.join(str(x) for x in self.board[i]))
            show.append("   "+"___ "*8)
        show.append("\t"+('{}\t'*8).format(*abc))
        return '\n'.join(show)

    def positioning(self, x1, y1, x2, y2):
        # vertical
        if abs(x1-x2) > 0:
            if x1 > x2:
                for i in range(x2, x1+1):
                    self.board[i][y1] = " "
            if x2 > x1:
                for i in range(x1, x2+1):
                    self.board[i][y2] = " "
        # horizontal
        elif abs(y1-y2) > 0:
            if y1 > y2:
                for i in range(y2, y1+1):
                    self.board[x2][i] = " "
            if y2 > y1:
                for i in range(y1, y2+1):
                    self.board[x2][i] = " "

    def win_position(self, player):
        if (sum([row.count("*") > 0 for row in self.board]) % 2 == 0 and
        sum([any([row[j] == "*" for row in self.board]) for j in range(len(self.board))]) % 2 == 0 or
        sum([row.count("*") > 0 for row in self.board]) % 2 != 0 and
        sum([any([row[j] == "*" for row in self.board]) for j in range(len(self.board))]) % 2 != 0):
            print("Выигрышная позиция у игрока - ", player.player)

    def check_win(self, player):
        if all([row.count(" ")==8 for row in self.board]) == True:
            print("Победил : ", player)
            return False
        return True

class SuperNim(object):

    def __init__(self):
        self.players = [Player(1), Player(2)]
        self.player = self.players[0]
        self.Board = Board()
    def switch(self):
        if self.player == self.players[0]:
            self.player = self.players[1]
        elif self.player == self.players[1]:
            self.player = self.players[0]

    def between_xy(self, x1, y1, x2, y2):
        check_list = []
        # vertical
        if abs(x1-x2) > 0:
            if x1 > x2:
                for i in range(x2+1, x1):
                    if self.Board.board[i][y2] == " ":
                        check_list.extend(self.Board.board[i][y2])
            if x2 > x1:
                for i in range(x1+1, x2):
                    if self.Board.board[i][y2] == " ":
                        check_list.extend(self.Board.board[i][y2])
        # horizontal
        elif abs(y1-y2) > 0:
            if y1 > y2:
                for i in range(y2+1, y1):
                    if self.Board.board[x2][i] == " ":
                        check_list.extend(self.Board.board[x2][i])
            if y2 > y1:
                for i in range(y1+1, y2):
                    if self.Board.board[x2][i] == " ":
                        check_list.extend(self.Board.board[x2][i])
        if len(check_list) > 0:
            self.player.decode_second(self.player.check_second(input("Ошибка, Ходить через пустые клетки нельзя.\n Введите координату :"), self.player.z))

    def check_nothing(self, x, y):
        if self.Board.board[x][y] == " ":
            self.player.decode_first(self.player.check_first(input("Нельзя начинать с пустой клетки, введите первые координаты :")))

    def game(self):
        while self.Board.check_win(self.player) != False:
            print(self.Board)
            self.player.x1, self.player.y1, self.player.z = self.player.decode_first(self.player.check_first(input("Введите координаты в формате \Число буква\ для горизонтали,\n \буква число\ для вертикали :")))
            while True:
                if self.Board.board[self.player.x1][self.player.y1] == " ":
                    self.player.x1, self.player.y1, self.player.z = self.player.decode_first(self.player.check_first(input("Нельзя начинать с пустой клетки, введите первые координаты :")))
                else:
                    break
            self.player.x2, self.player.y2 = self.player.decode_second(self.player.check_second(input("Точка пустая\nВведите координату, куда отправляемся : "), self.player.z))
            while True:
                if self.Board.board[self.player.x2][self.player.y2] == " ":
                    self.player.x2, self.player.y2 = self.player.decode_second(
                        self.player.check_second(input("Введите координату, куда отправляемся : "), self.player.z))
                else:
                    break
            self.between_xy(self.player.x1, self.player.y1, self.player.x2, self.player.y2)
            self.Board.positioning(self.player.x1, self.player.y1, self.player.x2, self.player.y2)
            self.Board.win_position(self.player)
            self.Board.check_win(self.player)
            self.switch()


s = SuperNim()
s.game()
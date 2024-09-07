# 6.	Реализовать программу, при помощи которой 2 игрока могут играть в игру «Клондайк».
# Правила игры следующие. Игра ведётся на игровом поле размером 10 на 10 клеток.
# Игроки по очереди выставляют в любую свободную клетку по отметке, и тот игрок,
# после чьего хода получилась цепочка длиной хотя бы в 3 отметке, проигрывает.
# При этом в цепочке считаются как свои отметки, так и отметки соперника,
# у игровых фишек как бы нет хозяина. Цепочка - это ряд фишек, следующая фишка в котором
# примыкает к предыдущей с любого из 8-ми направлений. (описание правил игры:
# https://www.iqfun.ru/printable-puzzles/klondike-igra.shtml )
# Взаимодействие с программой производится через консоль. Игровое поле изображается в
# виде 10 текстовых строк и перерисовывается при каждом изменении состояния поля.
# При запросе данных от пользователя программа сообщает, что ожидает от пользователя
# (например, координаты очередного хода) и проверяет корректность ввода.
# Программа должна уметь автоматически определять окончание партии и ее победителя.
# Сама программа НЕ ходит, т.е. не пытается ставить в клетки отметки с целью выиграть игру.

class Board(object):

    def __init__(self):
        self.board=[[" "]*10 for j in range(10)]

    def __str__(self):
        show= ["a   b   c   d   e   f   g   h   i   j"]
        for i in range(len(self.board)):
            show.append(' | '.join(self.board[i]) + f" ||{i+1}")
            show.append("____"*10)
        show.pop()
        return '\n'.join(show)

    def add_position(self, player, x, y):
        self.board[x][y] = player

    def check_win(self,player):
        for row in range(len(self.board)):
            for item in range(len(self.board[row])-2):
                if self.board[row][item]!=" " and self.board[row][item+1]!=" " and self.board[row][item+2]!=" ":
                    print("Победил : ",player.figure)
                    return False
        for row in range(len(self.board)-2):
            for item in range(len(self.board[row])):
                if self.board[row][item]!=" " and self.board[row+1][item]!=" " and self.board[row+2][item]!=" ":
                    print("Победил : ",player.figure)
                    return False
        for row in range(2, len(self.board)-2):
            for item in range(2, len(self.board[row])-2):
                if (self.board[row][item]!=" " and self.board[row+1][item+1]!=" " and self.board[row+2][item+2]!=" " or
                self.board[row][item]!=" " and self.board[row-1][item-1]!=" " and self.board[row-2][item-2]!=" " or
                self.board[row][item]!=" " and self.board[row+1][item-1]!=" " and self.board[row+2][item-2]!=" " or
                self.board[row][item]!=" " and self.board[row-1][item+1]!=" " and self.board[row-2][item+2]!=" "):
                    print("Победил : ",player.figure)
                    return False
        return True

class Player(object):

    def __init__(self,figure):
        self.figure = figure
        self.x,self.y="",""

    def __str__(self):
        return f"{self.figure},{self.x},{self.y}"

    abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    dig = [str(i+1) for i in range(10)]
    def check_input(self, xy):
        try:
            xy = xy.lower().split()
            if len(xy) != 2:
                raise Exception
            if (((any([elem == xy[0] for elem in self.abc]) == True) and (
                    any([elem == xy[1] for elem in self.dig]) != True)) or (
                    (any([elem == xy[0] for elem in self.dig]) == True) and (
                    any([elem == xy[1] for elem in self.abc]) != True))):
                raise Exception
            return xy

        except Exception:
            while True:
                print("Некорректные данные. Доступные данные : ", self.abc, self.dig)
                xy = input().lower().split()
                if len(xy) == 2:
                    if (((any([elem == xy[0] for elem in self.abc]) == True) and
                         (any([elem == xy[1] for elem in self.dig]) == True) or
                         (any([elem == xy[0] for elem in self.dig]) == True) and
                         (any([elem == xy[1] for elem in self.abc]) == True))):
                        return xy


    def change(self, xy):
        a, b = xy
        if any([elem == a for elem in self.dig]) == True:
            a, b = self.dig.index(a), self.abc.index(b)
        if any([elem == a for elem in self.abc]) == True:
            a, b = b, a
            a, b = self.dig.index(a), self.abc.index(b)
        return a, b

    def combine(self, xy):
        xy = self.check_input(xy)
        self.x, self.y = self.change(xy)
        return self.x, self.y
class Clondike(object):

    def __init__(self):
        self.BOARD = Board()
        self.players = [Player("X"),Player("O")]
        self.player = self.players[0]

    def switch(self):
        if self.player == self.players[0]:
            self.player = self.players[1]
        elif self.player == self.players[1]:
            self.player = self.players[0]

    def check_spot(self, x, y):
        if self.BOARD.board[int(x)][int(y)] != " ":
            while True:
                print("Выберите другое поле, это занято")
                x, y = self.player.combine(input())
                if self.BOARD.board[int(x)][int(y)] == " ":
                    return x, y

    def game(self):
        print(self.BOARD)
        while True:
            self.player.x, self.player.y = self.player.combine(input("Введите координаты : "))
            self.check_spot(self.player.x, self.player.y)
            self.BOARD.add_position(self.player.figure, self.player.x, self.player.y)
            self.switch()
            print(self.BOARD)
            a = self.BOARD.check_win(self.player)
            if a==False:
                print("Игра окончена!")
                break

c = Clondike()
c.game()
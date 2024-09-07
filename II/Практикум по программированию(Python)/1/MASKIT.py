# 7.	Реализовать программу , при помощи которой 2 игрока могут играть в игру «Максит». Правила игры следующие.
# В клетках квадрата 3 на 3 пишутся случайные числа из диапазона от 1 до 9. Начинающий выбирает любое
# понравившееся ему число и вычеркивает его, прибавляя к своей сумме. Второй игрок может выбрать любое из
# оставшихся чисел того столбца, в котором первый игрок делал свой предыдущий ход. Он тоже вычеркивает выбранное
# число, прибавляя его к своей сумме. Первый игрок далее поступает аналогично, выбирая число-кандидата из той строки,
# в которой второй игрок ходил перед этим. Может так случиться, что у какого-то игрока не будет хода. Тогда его
# соперник продолжает игру, делая ход в той же строке (для первого игрока) или в том же столбце (для второго игрока),
# что и до этого. Игра заканчивается, когда оба играющих не имеют ходов. Результат определяется по набранным суммам,
# у кого она больше, тот и выиграл. При равенстве сумм фиксируется ничья.
# (описание правил игры: https://www.iqfun.ru/articles/maxit.shtml ).
# Взаимодействие с программой производится через консоль. Игровое поле изображается в виде 3 текстовых строк и
# перерисовывается при каждом изменении состояния поля. При запросе данных от пользователя программа сообщает,
# что ожидает от пользователя (например, координаты очередного хода) и проверяет корректность ввода.
# Программа должна уметь автоматически определять сумму очков каждого из игроков и окончание партии и ее победителя.
# Сама программа НЕ ходит, т.е. не пытается вычеркивать числа с целью выиграть игру.

from random import randint

class Player(object):

    def __init__(self,figure):
        self.figure = figure
        self.x,self.y="",""
        self.score = 0

    def __str__(self):
        return f"{self.figure},{self.x},{self.y},{self.score}"

    def check_input_row(self,x):
        try:
            if len(x)==1:
                if any([str(i)==x for i in range(3)])==True:
                    return int(x)
                else:
                    raise Exception
            else:
                raise Exception
        except Exception:
            while True:
                print("ОШИБКА! Введите номер индекс строки")
                x = input()
                if len(x) == 1:
                    if any([str(i) == x for i in range(3)]) == True:
                        return int(x)

    def check_input_column(self,y):
        try:
            if len(y)==1:
                if any([str(i)==y for i in range(3)])==True:
                    return int(y)
                else:
                    raise Exception
            else:
                raise Exception
        except Exception:
            while True:
                print("Ошибка, нужен индекс колонны")
                y = input()
                if len(y) == 1:
                    if any([str(i) == y for i in range(3)]) == True:
                        return int(y)
class Board(object):

    def __init__(self):
        self.board = [[str(randint(1, 9)) for j in range(3)]for i in range(3)]

    def __str__(self):
        show=[]
        for i in range(len(self.board)):
            show.append(" | ".join(str(x) for x in self.board[i]))
        return "\n".join(show)

    def position(self,x,y):
        self.board[x][y]= " "

    def end_game(self,x,y):
        if all([row.count(" ")==0 for row in self.board])==True:
            print("Игра окончена")
            return False
        elif self.board[x].count(" ")==0 and self.board[0][y]==" " and self.board[1][y]==" " and self.board[2][y]==" ":
            print("Игра окончена")
            return False
        else:
            return True

class MASKIT(object):

    def __init__(self):
        self.BOARD=Board()
        self.players=[Player("X"),Player("O")]
        self.player = self.players[0]

    def switch(self):
        if self.player == self.players[0]:
            self.player = self.players[1]
        elif self.player == self.players[1]:
            self.player = self.players[0]

    def score(self,x,y):
        if self.BOARD.board[x][y]!=" ":
            self.player.score+=int(self.BOARD.board[x][y])

    def check_score(self,x,y):
        print("Победил ",max(self.players[0].score,self.players[1].score))

    def game(self):
        print(self.BOARD)
        self.player.x = self.player.check_input_row(input("Введите строку "))
        self.player.y = self.player.check_input_column(input("Введите колонну "))
        self.score(self.player.x, self.player.y)
        self.BOARD.position(self.player.x,self.player.y)
        y = self.player.y
        self.switch()
        while self.BOARD.end_game():
            print(self.BOARD)
            self.player.x = self.player.check_input_row(input("Введите строку "))
            self.score(self.player.x,y)
            self.BOARD.position(self.player.x, y)
            if self.BOARD.end_game()==False:
                self.check_score(self.player.x,y)
                self.BOARD.end_game()
                break
            x = self.player.x
            self.switch()
            print(self.BOARD)
            self.player.y = self.player.check_input_column(input("Введите колонну "))
            self.score(x,self.player.y)
            self.BOARD.position(x,self.player.y)
            if self.BOARD.end_game()==False:
                self.check_score(x, self.player.y)
                self.BOARD.end_game()
                break
            y = self.player.y
            self.switch()


m = MASKIT()
m.game()
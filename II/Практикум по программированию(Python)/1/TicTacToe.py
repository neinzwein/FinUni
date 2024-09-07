class Player(object):

    def __init__(self,figure):
        self.figure=figure
        self.x=''
        self.y=''

    abc, dig = ['a', 'b', 'c'], ['1', '2', '3']

    def __str__(self):
        return f"{self.x},{self.y}"

    # def __getattr__(self, item):
    #     return item

    def check_input(self, xy):
        try:
            xy = xy.lower().split()
            if len(xy) != 2:
                raise Exception
            if (((any([elem == xy[0] for elem in self.abc]) == True) and (any([elem == xy[1] for elem in self.dig]) != True)) or ((any([elem == xy[0] for elem in self.dig]) == True) and (any([elem == xy[1] for elem in self.abc]) != True))):
                raise Exception
            return xy

        except Exception:
            while True:
                print("Некорректные данные. Доступные данные : ", self.abc, self.dig)
                xy = input().lower().split()
                if len(xy) == 2:
                    if (((any([elem == xy[0] for elem in self.abc]) == True) and
                    (any([elem == xy[1] for elem in self.dig]) == True) or
                    #########Stealing Fat - The Dust Brothers###########
                    (any([elem == xy[0] for elem in self.dig]) == True) and
                    (any([elem == xy[1] for elem in self.abc]) == True))):
                        return xy
    #Меня всё время спрашивают, знаю ли я Тайлера Дердена
    def change(self, xy):
        a, b = xy
        if any([elem == a for elem in self.dig]) == True:
            a, b = self.dig.index(a),self.abc.index(b)
        if any([elem == a for elem in self.abc]) == True:
            a, b = b, a
            a, b = self.dig.index(a), self.abc.index(b)
        return a, b

    def combine(self, xy):
        xy = self.check_input(xy)
        self.x, self.y = self.change(xy)
        return self.x,self.y

class Board(object):

    def __init__(self):
        self.board=[[' ']*3 for i in range(3)]

    def __str__(self):
        show = [" A  B  C "]
        for i in range(len(self.board)):
            show.append(' | '.join(str(x) for x in self.board[i]) + f" {i + 1}")
            show.append('___'*3)
        show.pop()
        return '\n'.join(show)
    #
    # def __getitem__(self, item):
    #     return item

    def check_full(self):#Возвращает True, пока все поля не заняты
        return all([elem.count(' ') == 0 for elem in self.board]) == False

    def add_position(self, player, x, y):
        self.board[x][y] = player

    def check_win(self, player):
        # Горизонталь
        if any([row.count(player) == 3 for row in self.board]):
            print("Победил : ", player)
            return False
        # Диагональ
        if (all([row[i] == player for i, row in enumerate(self.board)]) == True or
        all([row[2-i] == player for i, row in enumerate(self.board)]) == True):
            print("Победил : ", player)
            return False
        # Вертикаль
        if (all([r[i-i] == player for i, r in enumerate(self.board)]) == True or
        all([r[i - i+1] == player for i, r in enumerate(self.board)]) == True or
        all([r[i - i+2] == player for i, r in enumerate(self.board)]) == True):
            print("Победил : ", player)
            return False
        return True

class TicTacToe(object):

    def __init__(self):
        self.Board = Board()
        self.players = [Player("X"),Player("O")]
        self.player = self.players[0]

    def switch_players(self):
        if self.player == self.players[0]:
            self.player = self.players[1]
            print("Очередь игрока : ", self.player.figure)
        elif self.player == self.players[1]:
            self.player = self.players[0]
            print("Очередь игрока : ", self.player.figure)

    def check_spot(self, x, y):
        if self.Board.board[x][y] != " ":
            while True:
                print("Выберите другое поле, это занято")
                x, y = self.player.combine(input())
                if self.Board.board[x][y] == " ":
                    return x, y
        return x, y

    def game(self):
        while True:
            print(self.Board)
            self.player.x,self.player.y = self.player.combine(input("Введите координаты : "))
            self.player.x, self.player.y = self.check_spot(self.player.x, self.player.y)
            self.Board.add_position(self.player.figure,self.player.x,self.player.y)
            self.Board.check_win(self.player.figure)
            a = self.Board.check_win(self.player.figure)
            if a == False:
                print("Игра окончена")
                break
            a = self.Board.check_full()
            if a == False:
                print("Ничья!")
                break
            self.switch_players()

t=TicTacToe()
t.game()
# b=Board()
# print(b,"Example")
# p=Player("X")
# b.add_position(p.figure,p.x,p.y)
# print(b)
# print(b.check_win(p.figure))
# 8.	(*) Реализовать программу, при помощи которой 2 игрока могут играть в игру «Мостики». Правила игры следующие.
# В ходе игры каждый из игроков старается построить мост с одного своего берега на другой по камням,
# образующим массив 4 на 5 (4 камня вдоль берега игрока и 5 камней между берегами). У первого игрока -
# крестики в качестве камней и берега крестиков (левый и правый край поля), у второго игрока – нолики и
# берега ноликов (верхний и нижний край поля). Игру можно начинать в любой точке поля. За один ход игрок
# может соединить два своих соседних камня вертикальным или горизонтальным мостиком (обозначаются в текстовом
# режиме символами «-» и «|»). Мосты первого и второго игрока пересекаться не должны. Выигрывает тот, кто
# построит непрерывный мост с одного своего берега на другой. (описание правил игры:
# https://www.7ya.ru/article/Chem-zanyat-rebenka-13-igr-na-liste-bumagi-so-slovami-kartinkami/ )
# Взаимодействие с программой производится через консоль. Игровое поле изображается в виде 9 текстовых строк
# и перерисовывается при каждом изменении состояния поля. При запросе данных от пользователя программа сообщает,
# что ожидает от пользователя (например, координаты очередного хода) и проверяет корректность ввода.
# Программа должна уметь автоматически определять недопустимые ходы (приводящие к пересечению мостов соперников)
# и окончание партии и ее победителя.
# Сама программа НЕ ходит, т.е. не пытается строить мосты с целью выиграть игру.
class player(object):

    def __init__(self,figure):
        self.figure = figure
        self.board = [[self.figure for i in range(4)] for j in range(5)]
        self.x1,self.y1,self.x2,self.y2=0,0,0,0
        self.way=[]

    def __str__(self):
        return f"{self.figure},{self.board}"

    # Вводятся x,y - нужно сделать проверку(от 0 до 3/4), проверку на соседние числа(вертикаль горизонталь)
    def input_X(self):
        try:
            if self.figure=="O":
                x = input("Введите строку : ")
                if any([str(i) == x for i in range(5)]):
                    return int(x)
                else:
                    raise ValueError
            elif self.figure=="X":
                x = input("Введите строку : ")
                if any([str(i) == x for i in range(4)]):
                    return int(x)
                else:
                    raise ValueError
        except ValueError:
            while True:
                if self.figure=="O":
                    print("Ошибка, выберите из "+f"{[str(i) for i in range(5)]}")
                    x = input("Введите строку : ")
                    if any([str(i) == x for i in range(5)]):
                        return int(x)
                elif self.figure=="X":
                    print("Ошибка, выберите из " + f"{[str(i) for i in range(4)]}")
                    x = input("Введите строку : ")
                    if any([str(i) == x for i in range(4)]):
                        return int(x)

    def input_Y(self):
        try:
            if self.figure=="O":
                y = input("Введите столбец : ")
                if any([str(i)==y for i in range(4)]):
                    return int(y)
                else:
                    raise ValueError
            elif self.figure=="X":
                y = input("Введите столбец : ")
                if any([str(i) == y for i in range(5)]):
                    return int(y)
                else:
                    raise ValueError
        except ValueError:
            while True:
                if self.figure=="O":
                    print("Ошибка, выберите из "+str([str(i) for i in range(4)]))
                    y = input("Введите столбец : ")
                    if any([str(i) == y for i in range(4)]):
                        return int(y)
                elif self.figure=="X":
                    print("Ошибка, выберите из " + str([str(i) for i in range(5)]))
                    y = input("Введите столбец : ")
                    if any([str(i) == y for i in range(5)]):
                        return int(y)

    def input_data(self):
        print("Первый камень")
        self.x1 = self.input_X()
        self.y1 = self.input_Y()
        print("Второй камень")
        self.x2 = self.input_X()
        self.y2 = self.input_Y()
        self.x1, self.x2 = min(self.x1, self.x2), max(self.x1, self.x2)
        self.y1, self.y2 = min(self.y1, self.y2), max(self.y1, self.y2)
        # return self.x1,self.y1,self.x2,self.y2

    # Переворачиваем
    def correction_X(self):
        if self.figure=="X":
            list = [[] for i in range(4)]
            for i in range(4):
                for j in range(5):
                    list[i].append(self.board[j][i])
            return list
    def check_neighboor(self):
        try:
            self.input_data()
            if abs(self.x2-self.x1)==0 and abs(self.y2-self.y1)==1:
                return self.x1,self.y1,self.x2,self.y2
            elif abs(self.x2-self.x1)==1 and abs(self.y2-self.y1)==0:
                return self.x1,self.y1,self.x2,self.y2
            else:
                raise Exception
        except Exception:
            while True:
                print("Только соседние можно соединить, вертикально или горизонтально. Попробуй ещё раз")
                self.input_data()
                if abs(self.x2-self.x1) == 0 and abs(self.y2-self.y1) == 1:
                    return self.x1,self.y1,self.x2,self.y2
                elif abs(self.x2-self.x1) == 1 and abs(self.y2-self.y1) == 0:
                    return self.x1,self.y1,self.x2,self.y2
    def position(self,x1:int,y1:int,x2:int,y2:int):
        if self.figure=="X":
            if self.board[y1][x1]==self.figure:
                self.board[y1][x1]=""
            if self.board[y2][x2]==self.figure:
                self.board[y2][x2]=""
            if abs(x2-x1)>0:
                if self.board[y1][x1].count("|")==0:
                    self.board[y1][x1]+="|"
                if self.board[y2][x2].count("|")==0:
                    self.board[y2][x2] += "|"
            else:
                if self.board[y1][x1].count("-")<2:
                    self.board[y1][x1]+="-"
                if self.board[y2][x2].count("-")<2:
                    self.board[y2][x2]+="-"
        elif self.figure=="O":
            if self.board[x1][y1]==self.figure:
                self.board[x1][y1]=""
            if self.board[x2][y2]==self.figure:
                self.board[x2][y2]=""
            if abs(x2-x1)>0:
                if self.board[x1][y1].count("|")==0:
                    self.board[x1][y1]+="|"
                if self.board[x2][y2].count("|")==0:
                    self.board[x2][y2]+="|"
            else:
                if self.board[x1][y1].count("-")<2:
                    self.board[x1][y1]+="-"
                if self.board[x2][y2].count("-")<2:
                    self.board[x2][y2]+="-"
    def ways(self,x1:int,y1:int,x2:int,y2:int):
        if self.figure=="O":
            self.way.append([x1,y1,x2,y2])
        elif self.figure=="X":
            self.way.append([y1,x1,y2,x2])
    def repeat_way(self):
        try:
            if self.figure=="X":
                if [self.y1,self.x1,self.y2,self.x2] in self.way:
                    raise ValueError
            elif self.figure=="O":
                if [self.x1,self.y1,self.x2,self.y2] in self.way:
                    raise ValueError
        except ValueError:
            while True:
                print("Повторяющийся ход, давай по новой")
                self.check_neighboor()
                if self.figure=="X":
                    if [self.y1,self.x1,self.y2,self.x2] not in self.way:
                        break
                elif self.figure=="O":
                    if [self.x1,self.y1,self.x2,self.y2] not in self.way:
                        break
class Game(object):

    def __init__(self):
        self.players=[player("X"),player("O")]
        self.player=self.players[0]
        self.way = self.players[0].way,self.players[1].way

    def __str__(self):
        show=[]
        columns = self.players[0].correction_X()
        for i in range(len(self.players[0].board)):
            show.append(f"\t"+"\t\t".join(str(x) for x in self.players[1].board[i])+f"\t\t\\{i}")
            if i<4:
                show.append("\t\t".join(str(x) for x in columns[i])+f"\t\\{i}")
        return '\n'.join(show)

    def switch(self):
        if self.player == self.players[0]:
            self.player = self.players[1]
        elif self.player == self.players[1]:
            self.player = self.players[0]

    def blocked_way(self):
        try:
            if self.player.figure=="X":
                if [self.player.y1,self.player.x1,self.player.y2,self.player.x2] in self.way[1]:
                    raise Exception
            elif self.player.figure=="O":
                if [self.player.x1,self.player.y1,self.player.x2,self.player.y2] in self.way[0]:
                    raise Exception
        except Exception:
            while True:
                print("Пусть преграждён, выберите другие камни")
                self.player.check_neighboor()
                self.player.repeat_way()
                if self.player.figure == "X":
                    if [self.player.y1, self.player.x1, self.player.y2, self.player.x2] not in self.way[1]:
                        break
                elif self.player.figure == "O":
                    if [self.player.x1, self.player.y1, self.player.x2, self.player.y2] not in self.way[0]:
                        break

    def check_win(self):
        counting=[[],[],[],[]]
        if self.player.figure=="X":
            for position in sorted(self.way[1]):
                for i in range(4):
                    counting[i].append(position[i])
                    counting[i] = sorted(counting[i])
            if counting[0] == [j for j in range(5)] and counting[2]==[j for j in range(5)]:
                print("Победитель -", self.player.figure)
                return False
        elif self.player.figure=="O":
            for position in sorted(self.way[0]):
                for i in range(4):
                    counting[i].append(position[i])
                    counting[i] = sorted(counting[i])
            if counting[0] == [j for j in range(5)] and counting[2] == [j for j in range(5)]:
                print("Победитель -", self.player.figure)
                return False

    def game(self):
        while True:
            print(self.__str__())
            print("Очередь " + self.player.figure)
            self.player.check_neighboor()
            self.player.repeat_way()
            self.blocked_way()
            self.player.position(self.player.x1,self.player.y1,self.player.x2,self.player.y2)
            self.player.ways(self.player.x1,self.player.y1,self.player.x2,self.player.y2)
            self.check_win()
            if self.check_win()==False:
                print("Игра окончена!")
                break
            self.switch()

g =Game()
g.game()

# 5.Реализовать программу, при помощи которой 3 игрока могут играть в игру «Лоскутное одеяло».
# Правила игры следующие. На поле, имеющем размер 4 на 5 клеток за один ход каждый игрок должен
# заполнить одну клетку своим символом. Игрок старается, чтобы его символы были как можно
# дальше друг от друга. В ходе игры ведется подсчет очков: за каждое соседство клеток с
# одинаковыми символами игроку, владельцу символа добавляется одно штрафное очко. Соседними
# считаются клетки, имеющие общую сторону или расположенные наискосок друг от друга.
# Выигрывает тот, у кого в конце игры меньше всего штрафных очков.
# Взаимодействие с программой производится через консоль. Игровое поле изображается в виде 4
# текстовых строк и перерисовывается при каждом изменении состояния поля.
# При запросе данных от пользователя программа сообщает, что ожидает от пользователя
# (например, координаты очередного хода) и проверяет корректность ввода.
# Программа должна уметь автоматически определять количество штрафных
# очков и окончание партии и ее победителя.
# Сама программа НЕ ходит, т.е. не пытается заполнять клетки символами с целью выиграть игру.

board = [[" " for i in range(5)]for j in range(4)]

players = ["X", "O", "I"]
players_score=[0,0,0]
player = players[0]

def show_board(board):
    show=[]
    for i in range(len(board)):
        show.append(' | '.join(board[i]) +"||"+ str(i))
        show.append("_"*18)
    show.pop()
    print('\n'.join(show))

def input_check(board, players):
    try:
        xy = input("Введите координаты (Строка - Номер)").lower().split()
        if len(xy)==2:
            if board[int(xy[0])][int(xy[1])] not in players and int(xy[0])<4 and int(xy[1])<5:
                return int(xy[0]), int(xy[1])
        else:
            raise Exception
    except Exception and IndexError and TypeError:
        print("Введены неверные данные")
        while True:
            xy = input("Введите координаты (Строка - Номер)").lower().split()
            if len(xy) == 2:
                if board[int(xy[0])][int(xy[1])] not in players and int(xy[0]) < 4 and int(xy[1]) < 5:
                    return int(xy[0]), int(xy[1])
def position(board,player,x,y):
    board[x][y]=player
    return board

def switch_player(players,player):
    if player == players[0]:
        player = players[1]
    elif player == players[1]:
        player = players[2]
    elif player == players[2]:
        player = players[0]
    return player

def Score(board,players,player,score):
    for i in range(len(board)):
        for j in range(len(board[i])-1):
            if board[i][j]==player and board[i][j+1]==player:
                score[players.index(player)]=int(score[players.index(player)])+1
    for i in range(len(board)-1):
        for j in range(len(board[i])):
            if board[i][j]==player and board[i+1][j]==player:
                score[players.index(player)] = int(score[players.index(player)]) + 1
    for i in range(len(board)-1):
        for j in range(1, len(board[i])-1):
            if board[i][j]==player and board[i+1][j-1]==player or board[i][j]==player and board[i+1][j+1]==player:
                score[players.index(player)] = int(score[players.index(player)]) + 1
    return score

def check_win(board,players,score):
    if all([row.count(" ")==0 for row in board]) == True:
        print("Победил",players[score.index(min(score))])

while True:
    show_board(board)
    x,y = input_check(board,players)
    board = position(board,player,x,y)
    players_score = Score(board,players,player,players_score)
    if check_win(board,players,players_score)==True:
        check_win(board, players, players_score)
        break
    player = switch_player(players,player)

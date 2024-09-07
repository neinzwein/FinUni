# 4.	Реализовать программу, с которой можно играть в игру «19».
# Правила игры следующие. Нужно выписать подряд числа от 1 до 19: в строчку до 9,
# а потом начать следующую строку, в каждой клетке по 1 цифре (не числу (см пример по ссылке)).
# Затем игроку необходимо вычеркнуть парные цифры или дающие в сумме 10. Условие -  пары должны
# находиться рядом или через зачеркнутые цифры по горизонтали или по вертикали.
# После того как все возможные пары вычеркнуты, оставшиеся цифры переписываются в конец таблицы.
# Цель - полностью вычеркнуть все цифры.
# (описание правил игры: http://podelki-fox.ru/igry-dlya-detey-na-bumage-s-chislami/ )
# Взаимодействие с программой производится через консоль.
# Игровое поле изображается в виде трех текстовых строк и перерисовывается при каждом
# изменении состояния поля. При запросе данных от пользователя программа сообщает,
# что ожидает от пользователя (в частности, координаты очередного хода) и проверяет
# корректность ввода. Программа должна уметь автоматически определять,
# что нужно выписать новые строки с цифрами и то, что партия окончена.
# Сама программа НЕ ходит, т.е. не пытается выбирать пары цифр с целью окончить игру.

# Создание доски курильщика
# board = [[1 if j==1 and i%2==1 else i//2 if j==1 and i%2==0 else 1 if j==2 and i%2==0 else i//2+5 if j==2 and i%2==1 else i for i in range(1, 10)]for j in range(3)]

# Создание доски нормального человека
def create_board():
    board = [[], [], []]
    for j in range(3):
        for i in range(1, 10):
            if j==1 and i%2==1:
                board[j].append(1)
            elif j==1 and i%2==0:
                board[j].append(i//2)
            elif j==2 and i%2==0:
                board[j].append(1)
            elif j==2 and i%2==1:
                board[j].append(i//2+5)
            else:
                board[j].append(i)
    return board

def check_divboard(board):
    box=[]
    c=0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != "0":
                box.append(board[i][j])
    return box

def continue_board(board,box):
    c = 0
    while c!=len(box):
        if len(board[len(board)-1])==9:
            board.append([])
        while len(board[len(board)-1])!=9:
            board[len(board)-1].append(box[c])
            c+=1
    else:
        return board

# Индексы в массиве
def check_pairs(board):
    pairs=[]
    # Для длины
    a = 0
    for i in range(len(board)):
        for j in range(len(board[i])-1):
            if board[i][j] != 0:
                a = board[i][j]
            if int(a) + int(board[i][j+1]) == 10 or a==board[i][j+1]:
                pairs.append([str(i), str(j), str(j+1)])
    # Для ширины
    b = 0
    for i in range(len(board)-1):
        for j in range(len(board)):
            if board[i][j] != 0:
                b = board[i][j]
            if int(b) + int(board[i+1][j]) == 10 or b == board[i+1][j]:
                pairs.append([str(i), str(i+1), str(j)])
    print(pairs)
    return pairs

def show_board(board):
    show = []
    for row in range(len(board)):
        show.append(' '.join([str(i) if i != 0 else " " for i in board[row]])+f" |{row}")
    print('\n'.join(show))

def input_position(pairs):
    try:
        print("Введите x1, y1, x2, y2")
        xy = input("СТРОКА1 - ЭЛЕМЕНТ1 - СТРОКА2 - ЭЛЕМЕНТ2 : ").lower().split()
        if len(xy)!=4:
            raise Exception
        if [xy[0], xy[2], xy[1]] in pairs or [xy[0], xy[1], xy[3]] in pairs:
            return xy[0], xy[1], xy[2], xy[3]
        else:
            print([xy[0], xy[2], xy[1]])
            raise Exception
    except Exception:
        while True:
            print("Ошибка, такой пары нет, введите данные ещё раз")
            xy = input("СТРОКА1 - ЭЛЕМЕНТ1 - СТРОКА2 - ЭЛЕМЕНТ2 : ").lower().split()
            if len(xy)==4:
                if [xy[0], xy[3], xy[1]] in pairs or [xy[0], xy[1], xy[3]] in pairs:
                    return xy[0], xy[1], xy[2], xy[3]

def delete_empty_row(board):
    for row in board:
        if all([str(i) == "0" for i in row]):
            del board[board.index(row)]
    return board
def check_win(board):
    if len(board)==0:
        print("Победа")
        return False
    else:
        return True

def positioning(board,x1,y1,x2,y2):
    board[int(x1)][int(y1)] = "0"
    board[int(x2)][int(y2)] = "0"
    return board


board = create_board()
while check_win(board)!=False:
    show_board(board)
    pairs = check_pairs(board)
    x1,y1,x2,y2 = input_position(pairs)
    board = positioning(board,x1,y1,x2,y2)
    if len(pairs) == 0:
        box = check_divboard(board)
        board = continue_board(board, box)
    board = delete_empty_row(board)
    check_win(board)
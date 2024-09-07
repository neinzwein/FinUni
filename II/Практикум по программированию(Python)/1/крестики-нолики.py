print("Крестики-нолики")
print("Правила: первый участник ходит крестиками, второй участник ходит ноликами")
print("Игрок поставивший 3 крестика/нолика в линию побеждает, иначе ничья")
print("Номера строк и столбцов начинаются с нуля")
print("Введите данные для определения размерности поля:n m(формат)")
def dem_board():
    try:
        input_=input().split()
        if len(input_)==2:
            n,m=input_[0],input_[1]
        if (n.isdigit() and m.isdigit()):
            if (int(n)<=2 or int(m)<=2):
                raise Exception
            else:
                return [int(n),int(m)]
        else:
            return [int(n),int(m)]
    except Exception:
        while True:
            print("Введены неверные данные")
            input_=input().split()
            if len(input_)==2:
                n,m=input_[0],input_[1]
            else:
                continue
            if (n.isdigit() and m.isdigit()):
                if  (int(n)>=3 and int(m)>=3):
                    break
            else:
                continue
        return [int(n),int(m)]
def input_coordinates(n,m):
    try:
        print('Введите данные для выбора клетки в формате:x y(вертикаль горизонталь)')
        input_=input().split()
        if len(input_)==2:
            x,y=input_[0],input_[1]
        if (x.isdigit() and y.isdigit()):
            if (int(x)>n or int(y)>m):
                raise Exception
            else:
                return [int(x),int(y)]
        else:
            return [int(x),int(y)]
    except Exception:
        while True:
            print("Введены неверные данные")
            input_=input().split()
            if len(input_)==2:
                x,y=input_[0],input_[1]
            else:
                continue
            if (x.isdigit() and y.isdigit()):
                if  (int(x)<=n and int(y)<=m):
                    break
            else:
                continue
        return [int(x),int(y)]
def print_board(board):
    for i in board:
        print(' '.join(i))
def write_cell(x,y,turn_index):
    cell_o,cell_x=[],[]
    if turn_index==0:
        cell_x.append([x,y])
    elif turn_index==1:
        cell_o.append([x,y])
    return cell_o,cell_x
def check_cell(board,cell_o,cell_x,n,m):
    res_o,res_x=0,0
    try:
        for index in range(len(cell_o)):
            a,b=int(board[index][0]),int(board[index][1])
            #вверх-вниз
            if board[a][b]=='O' and board[a-1][b]=='O' and board[a+1][b]=='O':
                res_o+=1
            #влево-вправо
            if board[a][b]=='O' and board[a][b-1]=='O' and board[a][b+1]=='O':
                res_o+=1
            #вниз-влево-вверх-вправо
            if board[a][b]=='O' and board[a+1][b-1]=='O' and board[a-1][b+1]=='O':
                res_o+=1
            #вниз-вправо-вверх-влево
            if board[a][b]=='O' and board[a+1][b+1]=='O' and board[a-1][b-1]=='O':
                res_o+=1
        for index in range(len(cell_x)):
            a,b=board[index][0],board[index][1]
            #вверх-вниз
            if board[a][b]=='X' and board[a-1][b]=='X' and board[a+1][b]=='X':
                res_x+=1
            #влево-вправо
            if board[a][b]=='X' and board[a][b-1]=='X' and board[a][b+1]=='X':
                res_x+=1
            #вниз-влево-вверх-вправо
            if board[a][b]=='X' and board[a+1][b-1]=='X' and board[a-1][b+1]=='X':
                res_x+=1
            #вниз-вправо-вверх-влево
            if board[a][b]=='X' and board[a+1][b+1]=='X' and board[a-1][b-1]=='X':
                res_x+=1
        return res_o,res_x
    except Exception:
        for i in range(1,n-1):
            for j in range(1,m-1):
                #вверх-вниз
                if board[i][j]=='O' and board[i-1][j]=='O' and board[i+1][j]=='O':
                    res_o+=1
                #влево-вправо
                if board[i][j]=='O' and board[i][j-1]=='O' and board[i][j+1]=='O':
                    res_o+=1
                #вниз-влево-вверх-вправо
                if board[i][j]=='O' and board[i+1][j-1]=='O' and board[i-1][j+1]=='O':
                    res_o+=1
                #вниз-вправо-вверх-влево
                if board[i][j]=='O' and board[i+1][j+1]=='O' and board[i-1][j-1]=='O':
                    res_o+=1
        for i in range(1,n-1):
            for j in range(1,m-1):
                #вверх-вниз
                if board[i][j]=='X' and board[i-1][j]=='X' and board[i+1][j]=='X':
                    res_x+=1
                #влево-вправо
                if board[i][j]=='X' and board[i][j-1]=='X' and board[i][j+1]=='X':
                    res_x+=1
                #вниз-влево-вверх-вправо
                if board[i][j]=='X' and board[i+1][j-1]=='X' and board[i-1][j+1]=='X':
                    res_x+=1
                #вниз-вправо-вверх-влево
                if board[i][j]=='X' and board[i+1][j+1]=='X' and board[i-1][j-1]=='X':
                    res_x+=1
        return res_o,res_x
def do_cell(x,y,turn_index,board):
    if turn_index==0:
        if board[x][y]=='.':
            for i in range(n):
                for j in range(m):
                    if (i==x and j==y):
                        board[i][j]='X'
            turn_index=1
        else:
            turn_index=0
    elif turn_index==1:
        if board[x][y]=='.':
            for i in range(n):
                for j in range(m):
                    if (i==x and j==y):
                        board[i][j]='O'
            turn_index=0
        else:
            turn_index=1
    return turn_index,board
#игра
turn_index=0
check_list=[]
O,X='O','X'
n,m=dem_board()
board=[['.']*n for i in range(m)]
print_board(board)
while True:
    a=input_coordinates(n,m)
    x,y=a
    cell_o,cell_x=write_cell(x,y,turn_index)
    res_o,res_x=check_cell(board,cell_o,cell_x,n,m)
    turn_index,board=do_cell(x,y,turn_index,board)
    print_board(board)
    if res_o!=0:
        print('Победа Ноликов')
        break
    elif res_x!=0:
        print('Победа Крестиков')
        break

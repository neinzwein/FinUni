print('Шахматы, Инструкция : игровое поле обозначено цифрами по вертикали и буквами по горизонтали, введите цифру и буквы (Пример : 2 A)')
#Выполнено : Мат, запись и считывание файла,ход назад
print('Инструкция: Сначала записывается позиция фигуры, которой будем ходить (число пробел буква), потом выбранную позицию. Чтобы посмотреть доступные команды - введите cmd')
desk =[[' ',' ','A','B','C','D','E','F','G','H',' ',' '],
       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
       ['8',' ','r','n','b','q','k','b','n','r',' ','8'],
       ['7',' ','p','p','p','p','p','p','p','p',' ','7'],
       ['6',' ','.','.','.','.','.','.','.','.',' ','6'],
       ['5',' ','.','.','.','.','.','.','.','.',' ','5'],
       ['4',' ','.','.','.','.','.','.','.','.',' ','4'],
       ['3',' ','.','.','.','.','.','.','.','.',' ','3'],
       ['2',' ','P','P','P','P','P','P','P','P',' ','2'],
       ['1',' ','R','N','B','Q','K','B','N','R',' ','1'],
       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
       [' ',' ','A','B','C','D','E','F','G','H',' ',' ']]
pass_num={'1','2','3','4','5','6','7','8'}
pass_char={'A','B','C','D','E','F','G','H'}
black=['r','n','b','q','k','p']
white=['R','N','B','Q','K','P']
turn_index=0
posible_position_k,posible_position_K=[],[]
pat=1
#Создание файла для записи
with open('Ходы.txt','w',newline='',encoding='utf-8') as f:
    f.close()
#Дозаписываем файл
def savefile(file,x1,y1,x2,y2,desk):
    with open(file,'a',newline='',encoding='utf-8') as f:
        f.write(str(x1)+' '+str(y1)+' '+desk[x1][y1]+' '+str(x2)+' '+str(y2)+' '+desk[x2][y2]+'\n')
#Считываем весь файл (команда read)
def readfile(file):
    with open(file,'r',newline='',encoding='utf-8') as f:
        reader=f.read().splitlines()
        for line in reader:
            print(line)
#Считываем файл с конца на сколько нам нужно(Например:back 3)
def readbackfile(file,ind):
    data_list=[]
    with open(file,'r',newline='',encoding='utf-8') as f:
        reader=f.read().splitlines()
        for line in range(len(reader),len(reader)-int(ind),-1):
            print(reader[line-1])
def readback(file,ind):
    data_list=[]
    with open(file,'r',newline='',encoding='utf-8') as f:
        reader=f.read().splitlines()
        for line in range(len(reader),len(reader)-int(ind),-1):
            data_list.append(reader[line-1])
        return data_list
#Расставляем фигуры по местам
def backstep(data_list):
    for i in range(len(data_list)):
        x1,y1,figure1,x2,y2,figure2=data_list[i].split(' ')
        desk[int(x1)][int(y1)]=figure1
        desk[int(x2)][int(y2)]=figure2
    return desk
def coordinates_check(desk):
    while True:
        #Вводим координаты и проверяем на допустимые значения
        coordinates=input()
        if (len(set(coordinates)&pass_num)==1 and len(set(coordinates)&pass_char))==1:
            x,y=coordinates.split()
                #Ищем позицию по обозначениям
            for i in range(len(desk)):
                if desk[i][0]==x:
                    x=i
                if desk[0][i]==y:
                    y=i
            return x,y
        elif 'back' in coordinates:
            if coordinates!='back':
                if len(coordinates.split(' '))==2:
                    back,ind=coordinates.split(' ')
                    readbackfile('Ходы.txt',ind)
        elif 'read' in coordinates:
            readfile('Ходы.txt')
        elif 'step' in coordinates:
            if coordinates!='step':
                if len(coordinates.split(' '))==2:
                    step,ind=coordinates.split(' ')
                    desk=backstep(readback('Ходы.txt',ind))
                    return desk
        elif coordinates=='cmd':
            print('read')
            print('Показывает все ходы в записи')
            print('back n')
            print('n - число, которое указывает сколько последних ходов показать')
            print('step n')
            print('n - число, на сколько ходов вернутся назад')
        else:
            print('Введен неверный формат позиции, введите ещё раз : ')
#Выводим доску
def printf(desk):
    for i in range(len(desk)):
        print(' '.join(desk[i])) 
#Проверка с вводом координат фигуры
def first_check(coordinates_check,turn_index):
    while True:
        print('Введите первую позицию : ')
        a=coordinates_check(desk)
        if len(str(a).split(' '))!=2:
            return desk
        else:
            x,y=a
            if (desk[x][y] in white and turn_index==0):
                return x,y
            elif (desk[x][y] in black and turn_index==1):
                return x,y
            else:
                print('Неправильная позиция, введите другую')
#Проверка с вводом вторых координат
def second_check(coordinates_check,turn_index):
    while True:
        print('Введите вторую позицию : ')
        a=coordinates_check(desk)
        if len(str(a).split(' '))!=2:
            return desk
        else:
            x,y=a
            if ((turn_index==1 and desk[x][y] in black) or (turn_index==1 and desk[x][y]=='.')):
                return x,y
            elif ((turn_index==0 and desk[x][y] in black) or (turn_index==0 and desk[x][y]=='.')):
                return x,y
            else:
                print('На этой позиции стоит ваша фигура, выберите другую позицию')
#Пат
def pat(pat,desk,posible_position_k,posible_position_K):
    pat=0
    for i in range(2,10):
        for j in range(2,10):
            if desk[i][j]=='p':
                if desk[i+1][j]=='.':
                    pat+=1
            if desk[i][j]=='P':
                if desk[i-1][j]=='.':
                    pat+=1
            if desk[i][j]=='r':
                if desk[i-1][j]=='.' or desk[i-1][j] in white:
                    pat+=1
                if desk[i+1][j]=='.' or desk[i+1][j] in white:
                    pat+=1
                if desk[i][j+1]=='.' or desk[i][j+1] in white:
                    pat+=1
                if desk[i][j-1]=='.' or desk[i][j-1] in white:
                    pat+=1
            if desk[i][j]=='R':
                if desk[i+1][j]=='.' or desk[i+1][j] in black:
                    pat+=1
                if desk[i+1][j]=='.' or desk[i+1][j] in black:
                    pat+=1
                if desk[i][j+1]=='.' or desk[i][j+1] in black:
                    pat+=1
                if desk[i][j-1]=='.' or desk[i][j-1] in black:
                    pat+=1
            if desk[i][j]=='n':
                if desk[i+2][j+1]=='.' or desk[i+2][j+1] in white:
                    pat+=1
                if desk[i+2][j-1]=='.' or desk[i+2][j-1] in white:
                    pat+=1
                if desk[i-2][j+1]=='.' or desk[i-2][j+1] in white:
                    pat+=1
                if desk[i-2][j-1]=='.' or desk[i-2][j-1] in white:
                    pat+=1
                if desk[i+1][j+2]=='.' or desk[i+1][j+2] in white:
                    pat+=1
                if desk[i+1][j-2]=='.' or desk[i+1][j-2] in white:
                    pat+=1
                if desk[i-1][j+2]=='.' or desk[i-1][j+2] in white:
                    pat+=1
                if desk[i-1][j-2]=='.' or desk[i-1][j-2] in white:
                    pat+=1
            if desk[i][j]=='N':
                if desk[i+2][j+1]=='.' or desk[i+2][j+1] in black:
                    pat+=1
                if desk[i+2][j-1]=='.' or desk[i+2][j-1] in black:
                    pat+=1
                if desk[i-2][j+1]=='.' or desk[i-2][j+1] in black:
                    pat+=1
                if desk[i-2][j-1]=='.' or desk[i-2][j-1] in black:
                    pat+=1
                if desk[i+1][j+2]=='.' or desk[i+1][j+2] in black:
                    pat+=1
                if desk[i+1][j-2]=='.' or desk[i+1][j-2] in black:
                    pat+=1
                if desk[i-1][j+2]=='.' or desk[i-1][j+2] in black:
                    pat+=1
                if desk[i-1][j-2]=='.' or desk[i-1][j-2] in black:
                    pat+=1
            if desk[i][j]=='b':
                if desk[i+1][j+1]=='.' or desk[i+1][j+1] in white:
                    pat+=1
                if desk[i+1][j-1]=='.' or desk[i+1][j-1] in white:
                    pat+=1
                if desk[i-1][j+1]=='.' or desk[i-1][j+1] in white:
                    pat+=1
                if desk[i-1][j-1]=='.' or desk[i-1][j-1] in white:
                    pat+=1
            if desk[i][j]=='B':
                if desk[i+1][j+1]=='.' or desk[i+1][j+1] in black:
                    pat+=1
                if desk[i+1][j-1]=='.' or desk[i+1][j-1] in black:
                    pat+=1
                if desk[i-1][j+1]=='.' or desk[i-1][j+1] in black:
                    pat+=1
                if desk[i-1][j-1]=='.' or desk[i-1][j-1] in black:
                    pat+=1
            if desk[i][j]=='q':
                if desk[i+1][j+1]=='.' or desk[i+1][j+1] in white:
                    pat+=1
                if desk[i+1][j-1]=='.' or desk[i+1][j-1] in white:
                    pat+=1
                if desk[i-1][j+1]=='.' or desk[i-1][j+1] in white:
                    pat+=1
                if desk[i-1][j-1]=='.' or desk[i-1][j-1] in white:
                    pat+=1
                if desk[i-1][j]=='.' or desk[i-1][j] in white:
                    pat+=1
                if desk[i+1][j]=='.' or desk[i+1][j] in white:
                    pat+=1
                if desk[i][j+1]=='.' or desk[i][j+1] in white:
                    pat+=1
                if desk[i][j-1]=='.' or desk[i][j-1] in white:
                    pat+=1
            if desk[i][j]=='Q':
                if desk[i+1][j+1]=='.' or desk[i+1][j+1] in black:
                    pat+=1
                if desk[i+1][j-1]=='.' or desk[i+1][j-1] in black:
                    pat+=1
                if desk[i-1][j+1]=='.' or desk[i-1][j+1] in black:
                    pat+=1
                if desk[i-1][j-1]=='.' or desk[i-1][j-1] in black:
                    pat+=1
                if desk[i+1][j]=='.' or desk[i+1][j] in black:
                    pat+=1
                if desk[i+1][j]=='.' or desk[i+1][j] in black:
                    pat+=1
                if desk[i][j+1]=='.' or desk[i][j+1] in black:
                    pat+=1
                if desk[i][j-1]=='.' or desk[i][j-1] in black:
                    pat+=1
            if desk[i][j]=='k':
                if len(posible_position_k)>1:
                    pat+=1
            if desk[i][j]=='K':
                if len(posible_position_K)>1:
                    pat+=1
    return pat
#Проверка позиции короля
def check_position_king(desk,turn_index):
    for i in range(len(desk)):
        for j in range(len(desk[i])):
            if desk[i][j]=='k':
                king_x,king_y=i,j
    for i in range(len(desk)):
        for j in range(len(desk[i])):
            if desk[i][j]=='K':
                king_X,king_Y=i,j
    return king_x,king_y,king_X,king_Y
#Проверка количества доступных для короля
def checkmate(king_x,king_y,king_X,king_Y):
    posible_position_k=[]
    posible_position_K=[]
    #для чёрных
    if desk[king_x][king_y+1]=='.' or desk[king_x][king_y+1] in white:
        posible_position_k.append([king_x,king_y+1])
    if desk[king_x][king_y-1]=='.' or desk[king_x][king_y-1] in white:
        posible_position_k.append([king_x,king_y-1])
    if desk[king_x-1][king_y+1]=='.' or desk[king_x-1][king_y+1] in white:
        posible_position_k.append([king_x-1,king_y+1])
    if desk[king_x-1][king_y-1]=='.' or desk[king_x-1][king_y-1] in white:
        posible_position_k.append([king_x-1,king_y-1])
    if desk[king_x-1][king_y]=='.' or desk[king_x-1][king_y] in white:
        posible_position_k.append([king_x-1,king_y])
    if desk[king_x+1][king_y+1]=='.' or desk[king_x+1][king_y+1] in white:
        posible_position_k.append([king_x+1,king_y+1])
    if desk[king_x+1][king_y-1]=='.' or desk[king_x+1][king_y-1] in white:
        posible_position_k.append([king_x+1,king_y-1])
    if desk[king_x+1][king_y]=='.' or desk[king_x+1][king_y] in white:
        posible_position_k.append([king_x+1,king_y])
    if desk[king_x][king_y]=='k':
        posible_position_k.append([king_x,king_y])
    #для белых
    if desk[king_X][king_Y+1]=='.' or desk[king_X][king_Y+1] in black:
        posible_position_K.append([king_X,king_Y+1])
    if desk[king_X][king_Y-1]=='.' or desk[king_X][king_Y-1] in black:
        posible_position_K.append([king_X,king_Y-1])
    if desk[king_X-1][king_Y+1]=='.' or desk[king_X-1][king_Y+1] in black:
        posible_position_K.append([king_X-1,king_Y+1])
    if desk[king_X-1][king_Y-1]=='.' or desk[king_X-1][king_Y-1] in black:
        posible_position_K.append([king_X-1,king_Y-1])
    if desk[king_X-1][king_Y]=='.' or desk[king_X-1][king_Y] in black:
        posible_position_K.append([king_X-1,king_Y])
    if desk[king_X+1][king_Y+1]=='.' or desk[king_X+1][king_Y+1] in black:
        posible_position_K.append([king_X+1,king_Y+1])
    if desk[king_X+1][king_Y-1]=='.' or desk[king_X+1][king_Y-1] in black:
        posible_position_K.append([king_X+1,king_Y-1])
    if desk[king_X+1][king_Y]=='.' or desk[king_X+1][king_Y] in black:
        posible_position_K.append([king_X+1,king_Y])
    if desk[king_X][king_Y]=='K':
        posible_position_K.append([king_X,king_Y])
    return posible_position_k,posible_position_K
#Пешка
def pawn(x1,y1,x2,y2):
    case_list=[]
    #Первый ход пешек
    #Снизу вверх
    if (x1==x2+2 and y1==y2 and desk[x1][y1] in white and x1==8):
        for i in range(x1,x2,-1):
            if desk[i][y1]!='.':
                case_list.append(desk[i][y1])
        if len(case_list)==1:
            desk[x2][y2]=desk[x1][y1]
            desk[x1][y1]='.'
        #Шах пешкой
        if (desk[x2-1][y2+1]=='k' and desk[x2][y2] in white):
            print('Шах')
        if (desk[x2-1][y2-1]=='k' and desk[x2][y2] in white):
            print('Шах')
        return desk
    #Сверху вниз
    elif (x1==x2-2 and y1==y1 and desk[x1][y1] in black and x1==3):
        for i in range(x2,x1-1,-1):
            if desk[i][y1]!='.':
                case_list.append(desk[i][y1])
        if len(case_list)==1:
            desk[x2][y2]=desk[x1][y1]
            desk[x1][y1]='.'
        #Шах пешкой
        if (desk[x2+1][y2+1]=='K' and desk[x2][y2] in black):
            print('Шах')
        elif (desk[x2+1][y2-1]=='K' and desk[x2][y2] in black):
            print('Шах')
        return desk
    #Ходьба
    if ((x1==x2+1 and y1==y2 and desk[x1][y1] in white) or (x1==x2-1 and y1==y1 and desk[x1][y1] in black)):
        desk[x2][y2]=desk[x1][y1]
        desk[x1][y1]='.'
        #Шах пешкой
        if (desk[x2-1][y2+1]=='k' and desk[x2][y2] in white):
            print('Шах')
        elif (desk[x2-1][y2-1]=='k' and desk[x2][y2] in white):
            print('Шах')
        if (desk[x2+1][y2+1]=='K' and desk[x2][y2] in black):
            print('Шах')
        elif (desk[x2+1][y2-1]=='K' and desk[x2][y2] in black):
            print('Шах')
        #Пешка превращается в ферзя
        if (desk[x2][y2] in white and x2==2):
            desk[x2][y2]='Q'
        elif (desk[x2][y2] in black and x2==9):
            desk[x2][y2]='q'
        return desk
    #Атака
    elif ((x1==x2+1 and abs(y1-y2)==1 and desk[x1][y1] in white) or (x1==x2-1 and abs(y1-y2)==1 and desk[x1][y1] in black)):
        desk[x2][y2]=desk[x1][y1]
        desk[x1][y1]='.'
        #Шах пешкой
        if (desk[x2-1][y2-1]=='k' and desk[x2][y2] in white):
            print('Шах')
        elif (desk[x2-1][y2+1]=='k' and desk[x2][y2] in white):
            print('Шах')
        elif (desk[x2+1][y2+1]=='K' and desk[x2][y2] in black):
            print('Шах')
        elif (desk[x2+1][y2-1]=='K' and desk[x2][y2] in black):
            print('Шах')
        #Пешка превращается в ферзя
        if (desk[x2][y2]=='p' and x2==9):
            desk[x2][y2]='q'
        elif (desk[x2][y2]=='P' and x2==2):
            desk[x2][y2]='Q'
        return desk
    else:
        return None
# список всех координат точек под ударом (Пешка)
def pawn_check(posible_position_k,posible_position_K):
    for i in range(2,10):
        for j in range(2,10):
            if desk[i][j]=='p':
                if [i+1,j+1] in posible_position_K:
                    posible_position_K.remove([i+1,j+1])
                if [i+1,i-1] in posible_position_K:
                    posible_position_K.remove([i+1,j-1])
            if desk[i][j]=='P':
                if ([i-1,j+1] in posible_position_k):
                    posible_position_k.remove([i-1,j+1])
                if ([i-1,j-1] in posible_position_k):
                    posible_position_k.remove([i-1,j-1])
    return posible_position_k,posible_position_K
#Ладья
def rook(x1,y1,x2,y2):
    case_list=[]
    if x1==x2 or y1==y2:
        #вертикаль
        if y1==y2:
            #Снизу вверх
            if x1>x2:
                for i in range(x1,x2,-1):
                    if desk[i][y1]!='.':
                        case_list.append(desk[i][y1])
            #Сверху вниз
            elif x2>x1:
                for i in range(x2,x1-1,-1):
                    if desk[i][y1]!='.':
                        case_list.append(desk[i][y1])
        #горизонталь
        if x1==x2:
            #слева направо
            if y1>y2:
                for i in range(y1,y2,-1):
                    if desk[x1][i]!='.':
                        case_list.append(desk[x1][i])
            #справа налево
            elif y2>y1:
                for i in range(y2,y1-1,-1):
                    if desk[x1][i]!='.':
                        case_list.append(desk[x1][i])
        if len(case_list)==1:
            desk[x2][y2]=desk[x1][y1]
            desk[x1][y1]='.'
            #Шах ладьей
            for i in range(2,10):
                if ((desk[i][y2] in black) or (desk[i][y2] in white)):
                    break
                else:
                    if (desk[i][y2]=='k' and desk[x2][y2] in white):
                        print('Шах')
                if ((desk[x2][i] in black) or (desk[x2][i] in white)):
                    break
                else:
                    if (desk[x2][i]=='k' and desk[x2][y2] in white):
                        print('Шах')
                if ((desk[i][y2] in black) or (desk[i][y2] in white)):
                    break
                else:
                    if (desk[i][y2]=='K' and desk[x2][y2] in white):
                        print('Шах')
                if ((desk[x2][i] in black) or (desk[x2][i] in white)):
                    break
                else:
                    if (desk[x2][i]=='K' and desk[x2][y2] in white):
                        print('Шах')
            return desk
    else:
        return None
# список всех координат точек под ударом (Ладья)
def rook_check(posible_position_k,posible_position_K):
    posible_r,posible_R=[],[]
    for i in range(2,10):
        for j in range(2,10):
            if desk[i][j]=='r':
                posible_r.append([i,j])
            elif desk[i][j]=='R':
                posible_R.append([i,j])
    for i in range(2):
        x_r,y_r=posible_r[i]
        x_R,y_R=posible_R[i]
        #Для черных
        for k in range(x_r,10):
            if desk[k][y_r] in black or desk[k][y_r] in white:
                break
            else:
                if [k,y_r] in posible_position_K:
                    posible_position_K.remove([k,y_r])
        for k in range(9,x_r,-1):
            if desk[k][y_r] in black or desk[k][y_r] in white:
                break
            else:
                if [k,y_r] in posible_position_K:
                    posible_position_K.remove([k,y_r])
        for k in range(y_r,10):
            if desk[x_r][k] in black or desk[x_r][k] in white:
                break
            else:
                if [x_r,k] in posible_position_K:
                    posible_position_K.remove([x_r,k])
        for k in range(9,y_r,-1):
            if desk[x_r][k] in black or desk[x_r][k] in white:
                break
            else:
                if [x_r,k] in posible_position_K:
                    posible_position_K.remove([x_r,k])
        #для белых
        for k in range(x_R,10):
            if desk[k][y_R] in black or desk[k][y_R] in white:
                break
            else:
                if [k,y_R] in posible_position_k:
                    posible_position_k.remove([k,y_R])
        for k in range(9,x_R,-1):
            if desk[k][y_R] in black or desk[k][y_R] in white:
                break
            else:
                if [k,y_R] in posible_position_k:
                    posible_position_k.remove([k,y_R])
        for k in range(y_R,10):
            if desk[x_R][k] in black or desk[x_R][k] in white:
                break
            else:
                if [x_R,k] in posible_position_k:
                    posible_position_k.remove([x_R,k])
        for k in range(9,y_R,-1):
            if desk[x_R][k] in black or desk[x_R][k] in white:
                break
            else:
                if [x_R,k] in posible_position_k:
                    posible_position_k.remove([x_R,k])
    return posible_position_k,posible_position_K
#Конь
def knight(x1,y1,x2,y2):
    if abs(x1-x2)==1 and abs(y1-y2)==2 or abs(x1-x2)==2 and abs(y1-y2)==1:
        if desk[x1][y1] in white:
            desk[x2][y2]='N'
            desk[x1][y1]='.'
        elif desk[x1][y1] in black:
            desk[x2][y2]='n'
            desk[x1][y1]='.'
        #Шах конём
        if desk[x2][y2] in white:
            if (desk[x2+2][y2+1]=='k'):
                print('Шах')
            elif (desk[x2+2][y2-1]=='k'):
                print('Шах')
            elif (desk[x2-2][y2+1]=='k'):
                print('Шах')
            elif (desk[x2-2][y2-1]=='k'):
                print('Шах')
            elif (desk[x2+1][y2+2]=='k'):
                print('Шах')
            elif (desk[x2+1][y2-2]=='k'):
                print('Шах')
            elif (desk[x2-1][y2+2]=='k'):
                print('Шах')
            elif (desk[x2-1][y2-2]=='k'):
                print('Шах')
        if desk[x2][y2] in black:
            if (desk[x2+2][y2+1]=='K'):
                print('Шах')
            elif (desk[x2+2][y2-1]=='K'):
                print('Шах')
            elif (desk[x2-2][y2+1]=='K'):
                print('Шах')
            elif (desk[x2-2][y2-1]=='K'):
                print('Шах')
            elif (desk[x2+1][y2+2]=='K'):
                print('Шах')
            elif (desk[x2+1][y2-2]=='K'):
                print('Шах')
            elif (desk[x2-1][y2+2]=='K'):
                print('Шах')
            elif (desk[x2-1][y2-2]=='K'):
                print('Шах')
        return desk
    else:
        return None
# список всех координат точек под ударом (Конь)
def knight_check(posible_position_k,posible_position_K):
    posible_n,posible_N=[],[]
    for i in range(2,10):
        for j in range(2,10):
            if desk[i][j]=='p':
                if [i+2,j+1] in posible_position_K:
                    posible_position_K.remove([i+2,j+1])
                if [i+2,i-1] in posible_position_K:
                    posible_position_K.remove([i+2,j-1])
                if [i-2,j+1] in posible_position_K:
                    posible_position_K.remove([i-2,j+1])
                if [i-2,j-1] in posible_position_K:
                    posible_position_K.remove([i-2,j-1])
                if [i+1,j+2] in posible_position_K:
                    posible_position_K.remove([i+1,j+2])
                if [i+1,i-2] in posible_position_K:
                    posible_position_K.remove([i+1,j-2])
                if [i-1,j+2] in posible_position_K:
                    posible_position_K.remove([i-1,j+2])
                if [i-1,j-2] in posible_position_K:
                    posible_position_K.remove([i-1,j-2])
            if desk[i][j]=='P':
                if [i+2,j+1] in posible_position_k:
                    posible_position_k.remove([i+2,j+1])
                if [i+2,i-1] in posible_position_k:
                    posible_position_k.remove([i+2,j-1])
                if [i-2,j+1] in posible_position_k:
                    posible_position_k.remove([i-2,j+1])
                if [i-2,j-1] in posible_position_k:
                    posible_position_k.remove([i-2,j-1])
                if [i+1,j+2] in posible_position_k:
                    posible_position_k.remove([i+1,j+2])
                if [i+1,i-2] in posible_position_k:
                    posible_position_k.remove([i+1,j-2])
                if [i-1,j+2] in posible_position_k:
                    posible_position_k.remove([i-1,j+2])
                if [i-1,j-2] in posible_position_k:
                    posible_position_k.remove([i-1,j-2])
    return posible_position_k,posible_position_K
#Слон
def bishop(x1,y1,x2,y2):
    case_list=[]
    if abs(x1-x2)==abs(y1-y2):
        #Вверх
        if x1>x2:
            #Влево
            if y1>y2:
                for i in range(abs(x1-x2)):
                    if desk[x1-i][y1-i]!='.':
                        case_list.append(desk[x1-i][y1-i])
                        if case_list==1:
                            if ((desk[x1-i][y1-i]=='k' and desk[x1][y1] in white) or (desk[x1-i][y1-i]=='K' and desk[x1][y1] in black)):
                                print('Шах')
            #Вправо
            elif y2>y1:
                for i in range(abs(x1-x2)):
                    if desk[x1-i][y1+i]!='.':
                        case_list.append(desk[x1-i][y1+i])
                        if case_list==1:
                            if ((desk[x1-i][y1+i]=='k' and desk[x1][y1] in white) or (desk[x1-i][y1+i]=='K' and desk[x1][y1] in black)):
                                print('Шах')
        #Вниз
        elif x2>x1:
            #Влево
            if x1>x2:
                for i in range(abs(y1-y2)):
                    if desk[x1+i][y1-i]!='.':
                        case_list.append(desk[x1+i][y1-i])
                        if case_list==1:
                            if ((desk[x1+i][y1-i]=='k' and desk[x1][y1] in white) or (desk[x1+i][y1-i]=='K' and desk[x1][y1] in black)):
                                print('Шах')
            #Вправо
            if x2>x1:
                for i in range(abs(y2-y1)):
                    if desk[x1+i][y1+i]!='.':
                        case_list.append(desk[x1+i][y1+i])
                        if case_list==1:
                            if ((desk[x1+i][y1+i]=='k' and desk[x1][y1] in white) or (desk[x1+i][y1+i]=='K' and desk[x1][y1] in black)):
                                print('Шах')
        if len(case_list)==1:
            desk[x2][y2]=desk[x1][y1]
            desk[x1][y1]='.'
            return desk
    else:
        return None
# список всех координат точек под ударом (Слон)
def bishop_check(posible_position_k,posible_position_K):
    posible_b,posible_B=[],[]
    for i in range(2,10):
        for j in range(2,10):
            if desk[i][j]=='b':
                posible_b.append([i,j])
            elif desk[i][j]=='B':
                posible_B.append([i,j])
    for i in range(2):
        x_n,y_n=posible_b[i]
        x_N,y_N=posible_B[i]
        #для черных
        #Вверх-вправо
        for k in range(1,9):
            if ((desk[x_n-k][y_n+k] in white) or (desk[x_n-k][y_n+k] in black) or (desk[x_n-k][y_n+k]==' ')):
                break
            else:
                if [x_n-k,y_n+k] in posible_position_K:
                    posible_position_K.remove([x_n-k,y_n+k])
        #Вниз-вправо
        for k in range(1,9):
            if ((desk[x_n+k][y_n+k] in white) or (desk[x_n+k][y_n+k] in black) or (desk[x_n+k][y_n+k]==' ')):
                break
            else:
                if [x_n+k,y_n+k] in posible_position_K:
                    posible_position_K.remove([x_n+k,y_n+k])         
        #Вниз-влево
        for k in range(1,9):
            if ((desk[x_n+k][y_n-k] in white) or (desk[x_n+k][y_n-k] in black) or (desk[x_n+k][y_n-k]==' ')):
                break
            else:
                if [x_n+k,y_n-k] in posible_position_K:
                    posible_position_K.remove([x_n+k,y_n-k])      
        #Вверх-влево
        for k in range(1,9):
            if ((desk[x_n-k][y_n-k] in white) or (desk[x_n-k][y_n-k] in black) or (desk[x_n-k][y_n-k]==' ')):
                break
            else:
                if [x_n-k,y_n-k] in posible_position_K:
                    posible_position_K.remove([x_n-k,y_n-k])
        #для белых
        #Вверх-вправо
        for k in range(1,9):
            if ((desk[x_N-k][y_N+k] in white) or (desk[x_N-k][y_N+k] in black) or (desk[x_N-k][y_N+k]==' ')):
                break
            else:
                if [x_N-k,y_N+k] in posible_position_k:
                    posible_position_k.remove([x_N-k,y_N+k])
        #Вниз-вправо
        for k in range(1,9):
            if ((desk[x_N+k][y_N+k] in white) or (desk[x_N+k][y_N+k] in black) or (desk[x_N+k][y_N+k]==' ')):
                break
            else:
                if [x_N+k,y_N+k] in posible_position_k:
                    posible_position_k.remove([x_N+k,y_N+k])         
        #Вниз-влево
        for k in range(1,9):
            if ((desk[x_N+k][y_N-k] in white) or (desk[x_N+k][y_N-k] in black) or (desk[x_N+k][y_N-k]==' ')):
                break
            else:
                if [x_N+k,y_N-k] in posible_position_k:
                    posible_position_k.remove([x_N+k,y_N-k])      
        #Вверх-влево
        for k in range(1,9):
            if ((desk[x_N-k][y_N-k] in white) or (desk[x_N-k][y_N-k] in black) or (desk[x_N-k][y_N-k]==' ')):
                break
            else:
                if [x_N-k,y_N-k] in posible_position_k:
                    posible_position_k.remove([x_N-k,y_N-k])
    return posible_position_k,posible_position_K
#Ферзь
def queen(x1,y1,x2,y2):
    case_list=[]
    if x1==x2 or y1==y2:
        #вертикаль
        if y1==y2:
            #Снизу вверх
            if x1>x2:
                for i in range(x1,x2,-1):
                    if desk[i][y1]!='.':
                        case_list.append(desk[i][y1])
            #Сверху вниз
            elif x2>x1:
                for i in range(x2,x1-1,-1):
                    if desk[i][y1]!='.':
                        case_list.append(desk[i][y1])
        #горизонталь
        if x1==x2:
            #слева направо
            if y1>y2:
                for i in range(y1,y2,-1):
                    if desk[x1][i]!='.':
                        case_list.append(desk[x1][i])
            #справа налево
            elif y2>y1:
                for i in range(y2,y1-1,-1):
                    if desk[x1][i]!='.':
                        case_list.append(desk[x1][i])
        if len(case_list)==1:
            desk[x2][y2]=desk[x1][y1]
            desk[x1][y1]='.'
            for i in range(2,10):
                if (desk[i][y2]=='k' and desk[x2][y2] in white):
                    print('Шах')
                elif (desk[x2][i]=='k' and desk[x2][y2] in white):
                    print('Шах')
                elif (desk[i][y2]=='K' and desk[x2][y2] in black):
                    print('Шах')
                elif (desk[x2][i]=='K' and desk[x2][y2] in black):
                    print('Шах')
            return desk
    elif abs(x1-x2)==abs(y1-y2):
        #Вверх
        if x1>x2:
            #Влево
            if y1>y2:
                for i in range(abs(x1-x2)):
                    if desk[x1-i][y1-i]!='.':
                        case_list.append(desk[x1-i][y1-i])
                        if case_list==1:
                            if ((desk[x1-i][y1-i]=='k' and desk[x1][y1] in white) or (desk[x1-i][y1-i]=='K' and desk[x1][y1] in black)):
                                print('Шах')
            #Вправо
            elif y2>y1:
                for i in range(abs(x1-x2)):
                    if desk[x1-i][y1+i]!='.':
                        case_list.append(desk[x1-i][y1+i])
                        if case_list==1:
                            if ((desk[x1-i][y1+i]=='k' and desk[x1][y1] in white) or (desk[x1-i][y1+i]=='K' and desk[x1][y1] in black)):
                                print('Шах')
        #Вниз
        elif x2>x1:
            #Влево
            if x1>x2:
                for i in range(abs(y1-y2)):
                    if desk[x1+i][y1-i]!='.':
                        case_list.append(desk[x1+i][y1-i])
                        if case_list==1:
                            if ((desk[x1+i][y1-i]=='k' and desk[x1][y1] in white) or (desk[x1+i][y1-i]=='K' and desk[x1][y1] in black)):
                                print('Шах')
            #Вправо
            if x2>x1:
                for i in range(abs(y2-y1)):
                    if desk[x1+i][y1+i]!='.':
                        case_list.append(desk[x1+i][y1+i])
                        if case_list==1:
                            if ((desk[x1+i][y1+i]=='k' and desk[x1][y1] in white) or (desk[x1+i][y1+i]=='K' and desk[x1][y1] in black)):
                                print('Шах')
        if len(case_list)==1:
            desk[x2][y2]=desk[x1][y1]
            desk[x1][y1]='.'
            return desk
    else:
        return None
# список всех координат точек под ударом (Ферзь)
def queen_check(posible_position_k,posible_position_K):
    posible_q,posible_Q=[],[]
    for i in range(2,10):
        for j in range(2,10):
            if desk[i][j]=='q':
                posible_q.append([i,j])
            elif desk[i][j]=='Q':
                posible_Q.append([i,j])
    for i in range(1):
        x_q,y_q=posible_q[i]
        x_Q,y_Q=posible_Q[i]
        #Для черных
        #Вдоль-поперёк
        for k in range(x_q,10):
            if desk[k][y_q] in black or desk[k][y_q] in white:
                break
            else:
                if [k,y_q] in posible_position_K:
                    posible_position_K.remove([k,y_q])
        for k in range(9,x_q,-1):
            if desk[k][y_q] in black or desk[k][y_q] in white:
                break
            else:
                if [k,y_q] in posible_position_K:
                    posible_position_K.remove([k,y_q])
        for k in range(y_q,10):
            if desk[x_q][k] in black or desk[x_q][k] in white:
                break
            else:
                if [x_q,k] in posible_position_K:
                    posible_position_K.remove([x_q,k])
        for k in range(9,y_q,-1):
            if desk[x_q][k] in black or desk[x_q][k] in white:
                break
            else:
                if [x_q,k] in posible_position_K:
                    posible_position_K.remove([x_q,k])
        #По диагонали
        #Вверх-вправо
        for k in range(1,9):
            if ((desk[x_q-k][y_q+k] in white) or (desk[x_q-k][y_q+k] in black) or (desk[x_q-k][y_q+k]==' ')):
                break
            else:
                if [x_q-k,y_q+k] in posible_position_K:
                    posible_position_K.remove([x_q-k,y_q+k])
        #Вниз-вправо
        for k in range(1,9):
            if ((desk[x_q+k][y_q+k] in white) or (desk[x_q+k][y_q+k] in black) or (desk[x_q+k][y_q+k]==' ')):
                break
            else:
                if [x_q+k,y_q+k] in posible_position_K:
                    posible_position_K.remove([x_q+k,y_q+k])         
        #Вниз-влево
        for k in range(1,9):
            if ((desk[x_q+k][y_q-k] in white) or (desk[x_q+k][y_q-k] in black) or (desk[x_q+k][y_q-k]==' ')):
                break
            else:
                if [x_q+k,y_q-k] in posible_position_K:
                    posible_position_K.remove([x_q+k,y_q-k])      
        #Вверх-влево
        for k in range(1,9):
            if ((desk[x_q-k][y_q-k] in white) or (desk[x_q-k][y_q-k] in black) or (desk[x_q-k][y_q-k]==' ')):
                break
            else:
                if [x_q-k,y_q-k] in posible_position_K:
                    posible_position_K.remove([x_q-k,y_q-k])
        #для белых
        #Вдоль-поперёк
        for k in range(x_Q,10):
            if desk[k][y_Q] in black or desk[k][y_Q] in white:
                break
            else:
                if [k,y_Q] in posible_position_k:
                    posible_position_k.remove([k,y_Q])
        for k in range(9,x_Q,-1):
            if desk[k][y_Q] in black or desk[k][y_Q] in white:
                break
            else:
                if [k,y_Q] in posible_position_k:
                    posible_position_k.remove([k,y_Q])
        for k in range(y_Q,10):
            if desk[x_Q][k] in black or desk[x_Q][k] in white:
                break
            else:
                if [x_Q,k] in posible_position_k:
                    posible_position_k.remove([x_Q,k])
        for k in range(9,y_Q,-1):
            if desk[x_Q][k] in black or desk[x_Q][k] in white:
                break
            else:
                if [x_Q,k] in posible_position_k:
                    posible_position_k.remove([x_Q,k])
        #По диагонали
        #Вверх-вправо
        for k in range(1,9):
            if ((desk[x_Q-k][y_Q+k] in white) or (desk[x_Q-k][y_Q+k] in black) or (desk[x_Q-k][y_Q+k]==' ')):
                break
            else:
                if [x_Q-k,y_Q+k] in posible_position_k:
                    posible_position_k.remove([x_Q-k,y_Q+k])
        #Вниз-вправо
        for k in range(1,9):
            if ((desk[x_Q+k][y_Q+k] in white) or (desk[x_Q+k][y_Q+k] in black) or (desk[x_Q+k][y_Q+k]==' ')):
                break
            else:
                if [x_Q+k,y_Q+k] in posible_position_k:
                    posible_position_k.remove([x_Q+k,y_Q+k])         
        #Вниз-влево
        for k in range(1,9):
            if ((desk[x_Q+k][y_Q-k] in white) or (desk[x_Q+k][y_Q-k] in black) or (desk[x_Q+k][y_Q-k]==' ')):
                break
            else:
                if [x_Q+k,y_Q-k] in posible_position_k:
                    posible_position_k.remove([x_Q+k,y_Q-k])      
        #Вверх-влево
        for k in range(1,9):
            if ((desk[x_Q-k][y_Q-k] in white) or (desk[x_Q-k][y_Q-k] in black) or (desk[x_Q-k][y_Q-k]==' ')):
                break
            else:
                if [x_Q-k,y_Q-k] in posible_position_k:
                    posible_position_k.remove([x_Q-k,y_Q-k])
    return posible_position_k,posible_position_K
#Король
def king(x1,y1,x2,y2):
    if abs(x1-x2)<=1 and abs(y1-y2)<=1:
        desk[x2][y2]=desk[x1][y1]
        desk[x1][y1]='.'
        #Ставить шах
        if ((desk[x2][y2] in white and desk[x2+1][y2+1]=='k')or(desk[x2][y2] in white and desk[x2+1][y2-1]=='k')or(desk[x2][y2] in white and desk[x2+1][y2]=='k')or(desk[x2][y2] in white and desk[x2-1][y2+1]=='k')or(desk[x2][y2] in white and desk[x2-1][y2-1]=='k')or(desk[x2][y2] in white and desk[x2-1][y2]=='k')or(desk[x2][y2] in white and desk[x2][y2+1]=='k')or(desk[x2][y2] in white and desk[x2][y2-1]=='k')):
            print('Шах')
        elif ((desk[x2][y2] in black and desk[x2+1][y2+1]=='K')or(desk[x2][y2] in black and desk[x2+1][y2-1]=='K')or(desk[x2][y2] in black and desk[x2+1][y2]=='K')or(desk[x2][y2] in black and desk[x2-1][y2+1]=='K')or(desk[x2][y2] in black and desk[x2-1][y2-1]=='K')or(desk[x2][y2] in black and desk[x2-1][y2]=='K')or(desk[x2][y2] in black and desk[x2][y2+1]=='K')or(desk[x2][y2] in black and desk[x2][y2-1]=='K')):
            print('Шах')
        return desk
    else:
        return None
# список всех координат точек под ударом (Король)
def king_check(posible_position_k,posible_position_K):
    posible_k,posible_K=[],[]
    for i in range(2,10):
        for j in range(2,10):
            if desk[i][j]=='k':
                posible_k.append([i,j])
            elif desk[i][j]=='K':
                posible_K.append([i,j])
    for i in range(1):
        x_k,y_k=posible_k[i]
        x_K,y_K=posible_K[i]
    #Для черных
        if [x_k+1,y_k+1] in posible_position_K:
            posible_position_K.remove([x_k+1,y_k+1])
        if [x_k+1,y_k] in posible_position_K:
            posible_position_K.remove([x_k+1,y_k])
        if [x_k+1,y_k-1] in posible_position_K:
            posible_position_K.remove([x_k+1,y_k-1])
        if [x_k,y_k+1] in posible_position_K:
            posible_position_K.remove([x_k,y_k+1])
        if [x_k,y_k-1] in posible_position_K:
            posible_position_K.remove([x_k,y_k-1])
        if [x_k-1,y_k+1] in posible_position_K:
            posible_position_K.remove([x_k-1,y_k+1])
        if [x_k-1,y_k] in posible_position_K:
            posible_position_K.remove([x_k-1,y_k])
        if [x_k-1,y_k-1] in posible_position_K:
            posible_position_K.remove([x_k-1,y_k-1])
    #для белых
        if [x_K+1,y_K+1] in posible_position_k:
            posible_position_k.remove([x_K+1,y_K+1])
        if [x_K+1,y_K] in posible_position_k:
            posible_position_k.remove([x_K+1,y_K])
        if [x_K+1,y_K-1] in posible_position_k:
            posible_position_k.remove([x_K+1,y_K-1])
        if [x_K,y_K+1] in posible_position_k:
            posible_position_k.remove([x_K,y_K+1])
        if [x_K,y_K-1] in posible_position_k:
            posible_position_k.remove([x_K,y_K-1])
        if [x_K-1,y_K+1] in posible_position_k:
            posible_position_k.remove([x_K-1,y_K+1])
        if [x_K-1,y_K] in posible_position_k:
            posible_position_k.remove([x_K-1,y_K])
        if [x_K-1,y_K-1] in posible_position_k:
            posible_position_k.remove([x_K-1,y_K-1])
    return posible_position_k,posible_position_K
#Конструируем
printf(desk)
while True:
    if turn_index==0:
        print('Черёд белых')
    elif turn_index==1:
        print('Черёд чёрных')
    while True:
        a=first_check(coordinates_check,turn_index)
        if type(a)==tuple:
            x1,y1=a
            break
        else:
            printf(desk)
            if turn_index==0:
                turn_index+=1
            elif turn_index==1:
                turn_index-=1
    while True:
        b=second_check(coordinates_check,turn_index)
        if type(b)==tuple:
            x2,y2=b
            break
        else:
            printf(desk)
            if turn_index==0:
                turn_index+=1
            elif turn_index==1:
                turn_index-=1
    figure1=desk[x1][y1]
    figure2=desk[x2][y2]
    savefile('Ходы.txt',x1,y1,x2,y2,desk)
    if desk[x1][y1]=='P':
        if (pawn(x1,y1,x2,y2)!=None and y2!=1 and y2!=0 and x2!=1 and x2!=0 and y2!=10 and y2!=11 and x2!=10 and x2!=11):
            pawn(x1,y1,x2,y2)
            turn_index+=1
    elif desk[x1][y1]=='p':
        if (pawn(x1,y1,x2,y2)!=None and y2!=1 and y2!=0 and x2!=1 and x2!=0 and y2!=10 and y2!=11 and x2!=10 and x2!=11):
            pawn(x1,y1,x2,y2)
            turn_index-=1
    elif desk[x1][y1]=='R':
        if (rook(x1,y1,x2,y2)!=None and y2!=1 and y2!=0 and x2!=1 and x2!=0 and y2!=10 and y2!=11 and x2!=10 and x2!=11):
            rook(x1,y1,x2,y2)
            turn_index+=1
    elif desk[x1][y1]=='r':
        if (rook(x1,y1,x2,y2)!=None and y2!=1 and y2!=0 and x2!=1 and x2!=0 and y2!=10 and y2!=11 and x2!=10 and x2!=11):
            rook(x1,y1,x2,y2)
            turn_index-=1
    elif desk[x1][y1]=='N':
        if (knight(x1,y1,x2,y2)!=None and y2!=1 and y2!=0 and x2!=1 and x2!=0 and y2!=10 and y2!=11 and x2!=10 and x2!=11):
            knight(x1,y1,x2,y2)
            turn_index+=1
    elif desk[x1][y1]=='n':
        if (knight(x1,y1,x2,y2)!=None and y2!=1 and y2!=0 and x2!=1 and x2!=0 and y2!=10 and y2!=11 and x2!=10 and x2!=11):
            knight(x1,y1,x2,y2)
            turn_index-=1
    elif desk[x1][y1]=='B':
        if (bishop(x1,y1,x2,y2)!=None and y2!=1 and y2!=0 and x2!=1 and x2!=0 and y2!=10 and y2!=11 and x2!=10 and x2!=11):
            bishop(x1,y1,x2,y2)
            turn_index+=1
    elif desk[x1][y1]=='b':
        if (bishop(x1,y1,x2,y2)!=None and y2!=1 and y2!=0 and x2!=1 and x2!=0 and y2!=10 and y2!=11 and x2!=10 and x2!=11):
            knight(x1,y1,x2,y2)
            turn_index-=1
    elif desk[x1][y1]=='Q':
        if (queen(x1,y1,x2,y2)!=None and y2!=1 and y2!=0 and x2!=1 and x2!=0 and y2!=10 and y2!=11 and x2!=10 and x2!=11):
            queen(x1,y1,x2,y2)
            turn_index+=1
    elif desk[x1][y1]=='q':
        if (queen(x1,y1,x2,y2)!=None and y2!=1 and y2!=0 and x2!=1 and x2!=0 and y2!=10 and y2!=11 and x2!=10 and x2!=11):
            queen(x1,y1,x2,y2)
            turn_index-=1
    elif desk[x1][y1]=='K':
        if (king(x1,y1,x2,y2)!=None and y2!=1 and y2!=0 and x2!=1 and x2!=0 and y2!=10 and y2!=11 and x2!=10 and x2!=11):
            king(x1,y1,x2,y2)
            turn_index+=1
    elif desk[x1][y1]=='k':
        if (king(x1,y1,x2,y2)!=None and y2!=1 and y2!=0 and x2!=1 and x2!=0 and y2!=10 and y2!=11 and x2!=10 and x2!=11):
            king(x1,y1,x2,y2)
            turn_index-=1
    king_x,king_y,king_X,king_Y=check_position_king(desk,turn_index)
    posible_position_k,posible_position_K=checkmate(king_x,king_y,king_X,king_Y)
    pawn_check(posible_position_k,posible_position_K)
    rook_check(posible_position_k,posible_position_K)
    knight_check(posible_position_k,posible_position_K)
    bishop_check(posible_position_k,posible_position_K)
    queen_check(posible_position_k,posible_position_K)
    king_check(posible_position_k,posible_position_K)
    pat(pat,desk,posible_position_k,posible_position_K)
    if len(posible_position_k)==0:
        print('Шах и мат!')
        print('Победили белые')
        break
    if len(posible_position_K)==0:
        print('Шах и мат!')
        print('Победили чёрные')
        break
    if pat==0:
        print('Пат')
        break
    printf(desk)

# Ребят, не помню, была где-то ошибка, а у меня 3 одинаковых файла, какой из них верный - не помню
# Загружаю на абум.
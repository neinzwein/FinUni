print("Крестики-нолики")
print("Правила: первый участник ходит крестиками, второй участник ходит ноликами")
print("Игрок поставивший 3 крестика/нолика в линию побеждает. Иначе ничья")
print("Номера строк и столбцов начинаются с нуля")
print("Введите имя первого участника:")
name_user_1=input()
print("Введите имя второго участника:")
name_user_2=input()
check=0
check_list=[]
game=True
answer=""
lines=[['' for i in range(3)]for j in range(3)]
def exam_win(dict_users):
    for key in dict_users:
        if lines[0][0]==dict_users[key] and lines[1][0]==dict_users[key] and lines[2][0]==dict_users[key]:
            print("Победил(а) "+key)
            return False
        elif lines[1][0]==dict_users[key] and lines[1][1]==dict_users[key] and lines[1][2]==dict_users[key]:
            print("Победил(а) "+key)
            return False
        elif lines[2][0]==dict_users[key] and lines[2][1]==dict_users[key] and lines[2][2]==dict_users[key]:
            print("Победил(а) "+key)
            return False
        elif lines[0][0]==dict_users[key] and lines[1][1]==dict_users[key] and lines[2][2]==dict_users[key]:
            print("Победил(а) "+key)
            return False
        elif lines[0][2]==dict_users[key] and lines[1][1]==dict_users[key] and lines[2][0]==dict_users[key]:
            print("Победил(а) "+key)
            return False
        elif lines[0][0]==dict_users[key] and lines[0][1]==dict_users[key] and lines[0][2]==dict_users[key]:
            print("Победил(а) "+key)
            return False
        elif lines[0][1]==dict_users[key] and lines[1][1]==dict_users[key] and lines[2][1]==dict_users[key]:
            print("Победил(а) "+key)
            return False
        elif lines[0][2]==dict_users[key] and lines[1][2]==dict_users[key] and lines[2][2]==dict_users[key]:
            print("Победил(а) "+key)
            return False
        elif check==9:
            print("Ничья!")
            return False
def exam_check_list(x,y,check_list):
    string=str(x)+str(y)
    while (string in check_list):
        print("Ошибка!")
        print("Поле занято или его нет! Пожалуйста, выберите другое место")
        x,y=[i for i in input().split()]
        string=str(x)+str(y)
        return [x,y]
digit_list=[]
def digit_exam(x,y):
    str_xy=str(x)+str(y)
    while(str_xy.isdigit()!=True):
        str_xy=x+y
        print("Ошибка!")
        print("Неправильные символы, введите еще раз : ")
        if (str_xy.isdigit()==False):
            x,y=[i for i in input().split()]
        elif (str_xy.isdigit()==True):
            digit_list.append(x)
            digit_list.append(y)
def check_game(exam_win):
    if exam_win(dict_users)==False:
        print("Игра окончена, хотите сыграть еще?")
        print("Введите 'да' или 'нет': ")
        answer=input()
        if answer=="да":
            game=True
            lines=[['' for i in range(3)]for j in range(3)]
        elif answer=="нет":
            game=False
        else:
            while answer!="да" or answer!="нет":
                print("Не понятно, пожалуйста, введите еще раз 'да' или 'нет' : ")
                answer=input()
            print("До встречи!)")
for j in lines:
    print(j)
while (game!=False):
    print("Ходит "+name_user_1)
    dict_users={name_user_1:'X'}
    print("Введите номер строки и номер столбца через пробел:")
    x,y=[i for i in input().split()]
    digit_exam(x,y)
    for i in digit_list:
        x=digit_list[0]
        y=digit_list[1]
    digit_list.clear()
    exam_check_list(int(x),int(y),check_list)
    check_list.append(str(x)+str(y))
    for i in range(3):
        for j in range(3):
            if i == int(x) and j == int(y):
                lines[i][j]='X'
    for j in lines:
        print(j)
    check+=1
    exam_win(dict_users)
    check_game(exam_win)
    print("Ходит "+name_user_2)
    dict_users={name_user_2:'0'}
    print("Введите номер строки и номер столбца через пробел:")
    x,y=[i for i in input().split()]
    digit_exam(x,y)
    for i in digit_list:
        x=digit_list[0]
        y=digit_list[1]
    digit_list.clear()
    exam_check_list(int(x),int(y),check_list)
    check_list.append(str(x)+str(y))
    for i in range(3):
        for j in range(3):
            if i==int(x) and j==int(y):
                lines[i][j]='0'
    for j in lines:
        print(j)
    check+=1
    exam_win(dict_users)
    check_game(exam_win)
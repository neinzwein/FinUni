import matplotlib.pyplot as plt
import itertools

#Рисует сами точки координат(Это в работе не нужно, а так для понимания)
#plt.scatter()
#Рисует от точек координат линию до другой точки
#plt.plot(arg)
#Не закрывает сразу окно(ждет действий пользователя)
#plt.show()

# На ввод поступает картеж картежей (например: ((0,0), (0,1), (1,1), (1,0)) – представление для квадрата)
# Что нам нужно сделать, раз картежи неизменяемые?
# Ответ - поменять тип данных


#Тут можно поступить сразу двумя, как я вижу способами:
#1)Сразу разделить на X и Y списки координат, либо
#2)просто перевести в список списков

# Для первого варианта :

#tuple_polygons = ((0,0), (0,1), (1,1), (1,0))

#polygons = ((0,0), (0,1), (1,1), (1,0))
polygons1=((0,2),(2,2),(2,0),(0,0))
polygons2=((1,2),(2,2),(1.5,3))
polygons3=((1,1),(0,2),(1,3),(2,3),(3,2),(2,1))

#list_polygons,x_list,y_list=[]
#for i in range(len(list_polygons)):
#    list_polygons.append(list(tuple_polygons[i]))
#for i in list_polygons:
#    x, y = i
#    x_list.append(x)
#    y_list.append(y)
#Зачем мы это делаем? - Ответ : Потому что линия делается от одной точки к другой и получается в данном случае н
#    x_list.append(x_list[0])
#    y_list.append(y_list[0])
#return x_list, y_list

def tupletolist(polygons):
    scatters_list,x_list,y_list=[],[],[]
    for i in range(0,len(polygons)):
        scatters_list.append(list(polygons[i]))
        print(scatters_list)
    for i in scatters_list:
        y,x=i
        x_list.append(x)
        y_list.append(y)
    x_list.append(x_list[0])
    y_list.append(y_list[0])
    return x_list,y_list

#def draw_figure(tupletolist,polygons):
#    x_list,y_list=tupletolist(polygons)
#    plt.plot(x_list,y_list)
#    plt.show()

def draw_figure_1(tupletolist,sub_iterations_x_3,sub_iterations_y_3,polygons):
    x_list,y_list=tupletolist(polygons)
    list_list_x,list_list_y=sub_iterations_x_3(tupletolist,polygons1,sub_iterations_x_2),sub_iterations_y_3(tupletolist,polygons1,sub_iterations_y_2)
    for i in range(len(list_list_x)):
        plt.plot(list_list_x[i],y_list)
    plt.show()

def draw_figure_2(polygons):
    x_list,y_list=tupletolist(polygons)
    list_list_y=iterations(tupletolist,polygons)
    for i in range(len(list_list_y)):
        plt.plot(x_list,list_list_y[i])
    plt.show()
#draw_figure_2(polygons1,iterations)
#draw_figure(tupletolist, polygons1)
#draw_figure(tupletolist, polygons2)

#draw_figure(tupletolist,polygons1)
#draw_figure(tupletolist,polygons2)
#draw_figure(tupletolist,polygons3)

#(1 вариант по 3 функции на х,у)
def sub_iterations_x_1(tupletolist,polygons):
    x_list,y_list=tupletolist(polygons)
    x_copy=[]
    max_x = max(itertools.chain(x_list))
    #Шаг = 2, увеличиваем
    for i in range(len(x_list)):
        x_copy.append(float(x_list[i]) + float(max_x) + 2)
    return x_copy

#print(sub_iterations_x_1(tupletolist,polygons1))

def sub_iterations_x_2(tupletolist,polygons,sub_iterations_x_1):
    x_list,y_list=tupletolist(polygons)
    x_copy_list=[]
    x_copy_list.append(x_list)
    for i in range(1,7):
        x_copy = sub_iterations_x_1(tupletolist, polygons)
        x_copy_list.append(x_copy)
    return x_copy_list

#print(sub_iterations_x_2(tupletolist,polygons1,sub_iterations_x_1))

def sub_iterations_x_3(tupletolist,polygons,sub_iterations_x_2):
    x_list, y_list = tupletolist(polygons)
    x_copy_list=sub_iterations_x_2(tupletolist,polygons,sub_iterations_x_1)
    max_x = max(itertools.chain(x_list))
    for i in range(2,7):
        for j in range(len(x_copy_list[i])):
            x_copy_list[i][j]=float(x_copy_list[i-1][j]) + float(max_x) + 2
    return (x_copy_list)

#print(sub_iterations_x_3(tupletolist, polygons1, sub_iterations_x_2))

def sub_iterations_y_1(tupletolist,polygons):
    x_list,y_list=tupletolist(polygons)
    y_copy=[]
    max_y = max(itertools.chain(y_list))
    #Шаг = 2, увеличиваем
    for i in range(len(y_list)):
        y_copy.append(float(y_list[i]) + float(max_y) + 2)
    return y_copy

#print(sub_iterations_y_1(tupletolist,polygons1))

def sub_iterations_y_2(tupletolist,polygons,sub_iterations_y_1):
    x_list,y_list=tupletolist(polygons)
    y_copy_list=[]
    y_copy_list.append(y_list)
    for i in range(1,7):
        y_copy = sub_iterations_y_1(tupletolist, polygons)
        y_copy_list.append(y_copy)
    return y_copy_list

#print(sub_iterations_y_2(tupletolist,polygons1,sub_iterations_y_1))

def sub_iterations_y_3(tupletolist,polygons,sub_iterations_y_2):
    x_list, y_list = tupletolist(polygons)
    y_copy_list=sub_iterations_y_2(tupletolist,polygons,sub_iterations_y_1)
    max_y = max(itertools.chain(y_list))
    for i in range(2,7):
        for j in range(len(y_copy_list[i])):
            y_copy_list[i][j]=float(y_copy_list[i-1][j]) + float(max_y) + 2
    return y_copy_list

#print(sub_iterations_y_3(tupletolist,polygons1,sub_iterations_y_2))

#По игрикам (2 вариант, вместо 6 функций)
def iterations(tupletolist,polygons):
    x_list,y_list=tupletolist(polygons)
    correct_y_list=[]
    #Шаг = 2
    print("Введите количество фигур")
    try:
        n=input()
    except Exception:
        while type(n)!=int:
            print("Введеное значение не является целым")
            n=int(input())
    correct_y_list.append(y_list)
    for i in range(1,int(n)):
#        max_y=max(itertools.chain(correct_y_list[i]))
        #в списке y_list с каждым его членом(у) производится операция
        new_y_list=list(map(lambda y: y + i*2, y_list))
        correct_y_list.append(new_y_list)
    return correct_y_list

#print(iterations(tupletolist,polygons1))

#print(draw_figure_2(polygons1))

#draw_figure(tupletolist,sub_iterations_x_3, sub_iterations_y_3, polygons1)

#горизонтально по иксам
#1 вариант
def tr_translate_1(polygons):
    list_y=sub_iterations_y_3(tupletolist,polygons,sub_iterations_y_2)
    list_list_y=[]
    #Шаг = 2
    for i in range(7):
        new_list_y=list(map(lambda y: y + 2,list_y[i]))
        list_list_y.append(new_list_y)
    return list_list_y

#print(tr_translate_1(polygons1))

def draw_tr_translate_1(polygons):
    x_list,y_list=tupletolist(polygons)
    list_list_y=tr_translate_1(polygons)
    for i in range(len(list_list_y)):
        plt.plot(list_list_y[i],x_list)
    plt.show()
# print(draw_tr_translate_1(polygons1))

#2 вариант
# n = 0 по умолчанию
def tr_translate_2(polygons,n=0):
    #n = число фигур
    list_y,n=iterations(tupletolist,polygons)
    list_list_y=[]
    #Шаг = 2
    for i in range(int(n)):
        new_list_y=list(map(lambda x: x + 2,list_y[i]))
        list_list_y.append(new_list_y)
    return list_list_y

#print(tr_translate_2(polygons1))


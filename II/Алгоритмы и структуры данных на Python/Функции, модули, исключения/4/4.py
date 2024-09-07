# Напишите функцию для решения уравнений степени не выше второй (квадратные и линейные):
# • если у функции три аргумента, их надо трактовать как a, b и c в уравнении 𝑎𝑥2+𝑏𝑥+𝑐=0;
# • если два — как коэффициенты b и c в уравнении 𝑏𝑥+𝑐=0;
# • если один — как коэффициент c в уравнении 𝑐 = 0;
# • если список коэффициентов пуст или коэффициентов больше трёх, то функция должна вернуть None.
# Функция возвращает список, содержаний все корни уравнения (два, один или ни одного).
# Если корнем является любое значение x, функция возвращает список, содержащий символ «*» (т.е. ["*"]).

import math

def Function1(*args):
    if len(args)<=1 or len(args)>3: # len(args)==0,len(args)>3, len(args)==1
        return None
    elif len(args)==2:
        # по условию трактуем как bx+c=0, так как выбор между тремя вариантами невозможен
        b,c = args
        x = -c/b
        if x>0:
            return None
        else:
            return ['*']
    elif len(args)==3:
        # 𝑎𝑥2+𝑏𝑥+𝑐=0
        a,b,c = args
        D = b**2-4*a*c
        if D<0:
            return None
        elif D==0:
            return ["*"]
        else:
            return ["*","*"]
        
print(Function1(1))
print(Function1(1,2))
print(Function1(4,7,3))
print(Function1(1,2,3,4))

def Function2(String):
    list_indexes=[]
    a,b,c=0,0,0
    #Коэффициентов нет
    if (String.find("x")==-1):
        return None
    String=String.replace("x2","a")
    String=String.replace("x","b")
    #Изменяем знаки
    def sub_function1(String):
        String=String.split("=")
        String0=String[0]
        String1=list(String[1])
        if String1[0] != "-":
            String1.insert(0, "-")
        for i in range(1,len(String1)):
            if String1[i]=="+":
                String1[i]="-"
            elif String1[i]=="-":
                String1[i]="+"
        String0=String0+''.join(String1)
        return String0
    String=sub_function1(String)
    def sub_function2(a,b,c,String,list_indexes):
        for i in range(len(String)):
            if String[i]=="+":
                list_indexes.append(1)
            elif String[i]=="-":
                list_indexes.append(-1)
        String0=String.replace("+","-")
        String0=String0.split("-")
        if String0[0]=="":
            String0.pop(0)
            for i in range(len(String0)):
                if "a" in list(String0[i]):
                    if len(String0[i])>1:
                        String0[i]=str(String0[i])[:-1]
                        a=a+int(String0[i])*int(list_indexes[i])
                    else:
                        a=a+1*int(list_indexes[i])
                elif "b" in list(String0[i]):
                    if len(String0[i]) > 1:
                        String0[i] = str(String0[i])[:-1]
                        b = b + int(String0[i]) * int(list_indexes[i])
                    else:
                        b = b + 1 * int(list_indexes[i])
                elif ("a" not in list(String0[i]) and "b" not in list(String0[i])):
                    c = c + int(String0[i])*int(list_indexes[i])
        elif(String0[0]!=""):
            list_indexes.append(1)
            for i in range(len(String0)):
                if "a" in list(String0[i]):
                    if len(String0[i])>1:
                        String0[i]=str(String0[i])[:-1]
                        a=a+int(String0[i])*-int(list_indexes[i])
                    else:
                        a=a+1*int(list_indexes[i])
                elif "b" in list(String0[i]):
                    if len(String0[i]) > 1:
                        String0[i] = str(String0[i])[:-1]
                        b = b + int(String0[i]) * -int(list_indexes[i])
                    else:
                        b = b + 1 * int(list_indexes[i])
                elif ("a" not in list(String0[i]) and "b" not in list(String0[i])):
                    c = c + int(String0[i])*-int(list_indexes[i])
        return a,b,c
    a,b,c=sub_function2(a,b,c,String,list_indexes)
    if (a!=0):
        if (b!=0):
            if (c!=0):
                D=b*b-4*(a*c)
                if (D>0):
                    x1=(-b+math.sqrt(D))/2*a
                    x2=(-b-math.sqrt(D))/2*a
                    return [x1,x2]
                elif (D==0):
                    x=-b/(2*a)
                    return x
                elif (D<0):
                    return None
            if (c==0):
                x1=0
                x2=-b/a
                return [x1,x2]
        elif (b==0):
            if (c!=0):
                x=c/a
                print(x)
                x1=math.sqrt(x)
                x2=-math.sqrt(x)
                return [x1,x2]
            elif (c==0):
                x=0
                return [x]
    elif (a==0):
        if (b!=0):
            if (c!=0):
                x=b/-c
                return [x]
            elif (c==0):
                return None
        elif (b==0):
            return None

# print(Function2("4x2-20x+25=0"))
# print(Function2("2x2-6=0"))

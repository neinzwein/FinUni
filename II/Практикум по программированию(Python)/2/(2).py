#Используем словарь, так как это удобнее всего
dict_names=dict([("один",1),("два",2),("три",3),("четыре",4),("пять",5),("шесть",6),
("семь",7),("восемь",8),("девять",9),("десять",10),("одиннадцать",11),("двенадцать",12),
("тринадцать",13),("четырнадцать",14),("пятнадцать",15),("шестнадцать",16),("семнадцать",17),
("восемнадцать",18),("девятнадцать",19),("двадцать",20),("тридцать",30),("сорок",40),
("пятьдесят",50),("шестьдесят",60),("семьдесят",70),("восемьдесят",80),("девяносто",90),("сто",100),
("плюс","+"),("минус","-"),("умножить","*"),("открывается","("),("закрывается",")")])
print("Тестовый калькулятор, выполнил Дервук Максим ЗБ-ПИ20-1")
print("Калькулятор принимает двузначные числа и обрабатывает их")
print("Введите пример : ")
str_input=[str(i)for i in input().split()]
def calc(str_input):
#Создаем список лишних слов
    letters=["в","на","скобка"]
#очищаем список от лишних слов
    for letter in str_input:
        if letter in letters:
            str_input.remove(letter)
#Меняем слова на символы
    int_input=[]
    for i in range(len(str_input)):
        for x,y in dict_names.items():
            if str_input[i]==x:
                int_input.append(str(y))
#Делаем правильные числа, спустя строк 300 кода пришел к этому, самое простое
    for i in range(1,len(int_input)):
        if int_input[i].isdigit() and int_input[i-1].isdigit():
            int_input[i]=str(int(int_input[i-1])+int(int_input[i]))
            int_input[i-1]='del'
    while 'del' in int_input:
        int_input.remove('del')
#Проверка на знак первой скобки
    signs=['+','-','*']
    first_sign=""
    if int_input[0]=='-' and int_input[1]=='(':
        first_sign+='-'
        del int_input[0]
#Находим индексы скобок
    brackets_index=[]
    for i in range(len(int_input)):
        if int_input[i]=='(' or int_input[i]==')':
            brackets_index.append(i)
#Получаем пример в строковом виде (скобки)
    res_bracket=""
    res=[]
    for i in range(1,len(brackets_index),2):
        res_bracket=""
        x,y=brackets_index[i-1],brackets_index[i]
        for j in range(x,y+1):
            res_bracket+=str(int_input[j])
        res.append(res_bracket)
#Считаем то, что в скобках
    res_brackets=[]
    for i in range(len(res)):
        s=eval(''.join(res[i]))
        res_brackets.append(s)
#Если был первый знак до скобки, то добавляем
    if len(first_sign)==1:
        res_brackets[0]=first_sign+str(res_brackets[0])
#Получаем пример в строковом виде (вне скобок)
    under_brackets=[]
    ex=""
    if len(brackets_index)==2:
        for i in range(1,len(brackets_index)):
            ex=""
            x,y=brackets_index[i]+1,len(int_input)
            for j in range(x,y):
                ex+=int_input[j]
            under_brackets.append(ex)
    elif len(brackets_index)>2:
        brackets_index.append(len(int_input))
        for i in range(2,len(brackets_index),2):
            x,y=brackets_index[i-1]+1,brackets_index[i]
            ex=""
            for j in range(x,y):
                ex+=int_input[j]
            under_brackets.append(ex)
    list_result=[]
#Расставляем примеры и результаты по местам (если были скобки)
    if len(brackets_index)>0:
        if brackets_index[0]>2:
            for i in range(0,brackets_index[0]):
                list_result.append(int_input[i])
    if len(brackets_index)>0:
        if brackets_index[0]==0 or brackets_index[1]==0:
            for i in range(len(res)):
                list_result.append(str(res_brackets[i]))
                list_result.append(under_brackets[i])
        if brackets_index[0]>1:
            for i in range(len(under_brackets)):
                list_result.append(str(res_brackets[i]))
                list_result.append(under_brackets[i])
    result=""
#Если нет скобок, то считаем
    if len(brackets_index)==0:
        result="".join(int_input)
        list_result.append(result)
#Приводим все варианты выражения к строчному виду
    int_result="".join(list_result)
    int_result=eval(int_result)
    str_result=[]
#Проверяем на знак ответа
    if int_result<0:
        int_result*=-1
        str_result.append('-')
#Проверяем на разрядность ответа
    if int_result%10>=0:
        x=int_result%10
        str_result.append(int_result-int_result%10)
        str_result.append(int_result%10)
    int_result=str(int_result)
#переводим строчное представление ответа в слова
    end_result=[]
    for i in str_result:
        for x,y in dict_names.items():
            if i==y:
                end_result.append(x)
    end_result=' '.join(end_result)
    return end_result
print(calc(str_input))

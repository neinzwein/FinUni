#1 (Гаусс)
a = [[2,3,3,5],
     [2,2,2,3],
     [2,2,1,2],
     [2,2,1,1]]

b = [5,5,4,3]

class Gauss(object):

#Объявление переменных в экземпляре класса
    def __init__(self, a, b):
        self.a = a
        self.b = b

#Перенос строк по индексу
    def ChangeLine(self, line_a, line_b):
        self.a[line_a], self.a[line_b], self.b[line_a],self.b[line_b] = self.a[line_b], self.a[line_a], self.b[line_b], self.b[line_a]

#Умножение строки на строку
    def MultipleLine(self, line_a, line_b, multiple_n):
        self.a[line_a] = [(i + j * multiple_n) for i, j in zip(self.a[line_a],self[line_b])]
        self.b[line_a] += self.b[line_b] * multiple_n

#Деление строки на строку
    def DivLine(self, line_a, div):
        self.a[line_a] = [i / div for i in self.a[line_a]]
        self.b[line_a] /= div

#Вывод матрицы
    def __repr__(self):
        line=''
        for i in range(len(self.a)):
            line += ' '.join(str(x) for x in self.a[i])+'\t'
            line += "|"+''.join(str(self.b[i]))+'\t'+'\n'
        print(line)

    def __getitem__(self, item):
        return self.a[item]

    def Operations(self):
        n=0
        while (n < len(self.b)):
            CurLine=None
            for i in range(n,len(self.a)):
                if CurLine is None or abs(self.a[i][n]) > abs(self.a[CurLine][n]):
                    CurLine=i
            if CurLine is None:
                print("Решений нет")
                return None
  #          self.__repr__()
            if CurLine != n:
                self.ChangeLine(CurLine,n)
   #             self.__repr__()
            self.DivLine(n, self.a[n][n])
  #          self.__repr__()
            for i in range(n+1,len(self.a)):
                self.MultipleLine(i, n, -self.a[i][n])
  #          self.__repr__()
            n+=1
        Res = [0 for i in self.b]
        for i in range(len(self.b)-1,-1,-1):
            Res[i] = self.b[i] - sum(k * m for k, m in zip(Res[(i+1):], self.a[i][(i+1):]))
        return Res

pt=Gauss(a, b)
result=pt.Operations()
for i in range(len(result)):
    print("x"+str(i+1)+' =\t'+str(result[i]))

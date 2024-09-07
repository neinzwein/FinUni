#1 Зейдель

a = [[2,3,3,5],
     [2,2,2,3],
     [2,2,1,2],
     [2,2,1,1]]

b = [5,5,4,3]

class Zeidel(object):

    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __repr__(self):
        line = ''
        for i in range(len(self.a)):
            line += ' '.join(str(x) for x in self.a[i]) + '\t'
            line += "|" + ''.join(str(self.b[i])) + '\t' + '\n'
        print(line)

    def __getitem__(self, item):
        return self.a[item]

    def Operations(self):
        array=[0 for i in range(len(self.a))]
        n = 0
        false = False
        s = 0
        while not false:
            array_c=array
            for i in range(len(self.a)):
                s1 = sum(self.a[i][j] * array_c[j] for j in range(i))
                s2 = sum(self.a[i][j] * array[j] for j in range(i + 1, len(self.a)))
                array_c[i] = (self.b[i] - s1 - s2) / self.a[i][i]
            s = sum(abs(array_c[i] - array[i]) for i in range(len(self.a)))
            false = s < 1e-6
            n += 1
            array = array_c
        return array

pt=Zeidel(a,b)
result = pt.Operations()
for i in range(len(result)):
    print("x"+str(i+1)+" = "+str(result[i]))
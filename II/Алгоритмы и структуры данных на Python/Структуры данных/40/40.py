# Реализовать структуру "Очередь". Сформировать две очереди с элементами - строками (например: названиями компаний-клиентов).
# Написать функцию, которая удаляет из второй очереди клиентов, стоящих также и в первой.

# Дополнение. Структура "Очередь" должна быть очередью по операциям добавления и удаления элементов.
# А по доступу на чтение элементов структура "Очередь" должна представлять собой линейный связный однонаправленный список.


#Fifo требуется

class Queue:

    def __init__(self) -> None:
        self.queue=[]

    def __str__(self) -> str:
        return f"{self.queue}"

    #добавляем элемент в конец очереди
    def enqueue(self,item):
        self.queue.append(item)

    #удаляем первый элемент очереди
    def dequeue(self):
        if len(self.queue)<1:
            return None
        return self.queue.pop(0)
    
    def size(self)->int:
        return len(self.queue)
    
def same(q1:Queue,q2:Queue)->None:
    
    tmp_queue = Queue()
    tmp1, tmp2 = 0,0
# set()-----------
    z1=0

    while z1<q1.size():
        tmp1 = q1.dequeue()
        z2=0

        while z2<q2.size():
            tmp2 = q2.dequeue()

            if tmp1!=tmp2:
                tmp_queue.enqueue(tmp2)

            z2+=1
# set() -----------

        while tmp_queue.size()!=0:
            q2.enqueue(tmp_queue.dequeue())

        q1.enqueue(tmp1)
        z1+=1

if __name__ == "__main__":

    q1 = Queue()
    q2 = Queue()

    for i in range(10):
        q1.enqueue(str(i))
        q2.enqueue(str(i+i))

    # print(q1,'\n',q2)
    same(q1,q2)
    print('\n',q1,"\n",q2)

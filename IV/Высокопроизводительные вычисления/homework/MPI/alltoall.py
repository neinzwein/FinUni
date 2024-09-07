#Вариант 1: Напишите программу, которая использует функцию alltoall,
# чтобы распределить данные между всеми процессами в коммуникаторе.
#  Каждый процесс должен создать массив случайных чисел и отправить его всем другим процессам.
#  Затем каждый процесс должен обработать полученные данные (например, вычислить среднее значение),
#  отсортировать полученные данные и отправить результаты обратно всем процессам с помощью alltoall.
#  В конце каждый процесс должен вывести исходные и полученные данные, а также результаты обработки;

from mpi4py import MPI
from random import randint

# mpirun -n 5 python3 alltoall.py

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

data = [randint(0,10) for i in range(size)] # Размерность должна быть одинакова у матрицы
print("Изначальный rank - %s, data - %s" %(rank,data))

comm.Barrier() # пусть будет для красоты

# Превращение в Т-матрицу(Внимание, все методы alltoall транспонируют)
tdata = comm.alltoall(data) # отправляем всем и принимаем всеми i-0++,j-rank 

dmean = sum(tdata)/len(tdata) # Проводим махинации
sortdata = sorted(tdata)

print("Вычислительный rank : %s, data : %s, mean : %s"%(rank, sortdata, dmean))

data = comm.alltoall(sortdata) 

if __name__=="__main__":
    for i in range(size):
        if rank == i:
            print("Итоговый rank : %s, data : %s"%(rank, data))
        comm.Barrier()

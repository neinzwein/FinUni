#Вариант 1: Напишите программу, которая использует функцию reduce, чтобы найти минимальное значение среди всех значений,
#  сгенерированных всеми процессами. Каждый процесс должен сгенерировать случайное число. 
# Затем используйте reduce с операцией MPI.MIN, чтобы найти минимальное значение. 
# В конце процесс с рангом 0 должен вывести минимальное значение;

from mpi4py import MPI
from random import randint

# mpirun -n 5 python3 reduce.py

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

data = randint(1,50)
print(f'rank - {rank}, init data - {data}')

comm.Barrier()

data = comm.reduce(sendobj=data,op = MPI.MIN) # op - функция. Возвращается всё в 0 ранк

print(f'rank - {rank}, res data - {data}')
#educe(sendbuf, recvbuf, rank_of_root_process, op = MPI.MIN)
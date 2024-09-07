#Вариант 1: Использование comm.scatter для распределения данных Напишите программу на Python,
#  используя модуль mpi4py, которая создает список чисел на процессе с рангом 0 и затем распространяет
#  эти числа на все остальные процессы с помощью функции comm.scatter. 
# Каждый процесс должен получить одно число из списка.
#  После получения числа каждый процесс должен выводить свой ранг и полученное число.

from mpi4py import MPI

# mpirun -n 5 python3 scatter.py
# list size значений, в данном случае 5

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
    data = [int(i) for i in range(1, size+1)] #Чтобы не терялись данные, когда задаём количество процессов, сделаем так
    print(f"Изначальный Пул : {rank}, изначальные данные : {data}")
else:
    data = None

if __name__ =="__main__":
    data = comm.scatter(data,root=0)
    print(f"Пул : {rank}, данные : {data}")
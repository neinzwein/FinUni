#Вариант 1: Использование comm.scatter и comm.gather для обработки данных Напишите программу на Python,
#  используя модуль mpi4py, которая создает список чисел на процессе с рангом 0,
#  распространяет эти числа на все процессы с помощью функции comm.scatter,
#  затем каждый процесс увеличивает свое число на 1 и собирает обновленные числа обратно на процессе 
# с рангом 0 с помощью функции comm.gather. На процессе с рангом 0 должен быть выведен исходный
#  список чисел и обновленный список чисел.

from mpi4py import MPI

# mpirun -n 5 python3 gather.py

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
    data = [int(i) for i in range(size)]
else:
    data = None

if __name__=="__main__":
    data = comm.scatter(data, root=0) #root откуда + разбиваем по процессам
    # print(f"Номер процесса : {rank}, список : {data}")
    data+=1
    newdata = comm.gather(data, root=0) #root куда + собираем по процессам
    if rank == 0:
        print(f"Номер процесса : {rank}, список : {newdata}")
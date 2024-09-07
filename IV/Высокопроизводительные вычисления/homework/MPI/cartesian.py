# Вариант 1: Реализуйте на MPI разбиение процессов приложения на две группы, 
# в одной из которых осуществляется обмен по кольцевой топологии, а в другой 
# – коммуникации по схеме «мастер – рабочие» (с использованием любых изученных функций).

from mpi4py import MPI

# mpirun -n 8 python3 cartesian.py

if __name__=="__main__":

    # кольцо - это одномерный тип топологии, но применим на все мерности, последний процессор -> первый
    # мастер - одномерное, аналогично с кольцом и измерениями, рабочие и мастер = звезда (от 1 ко всем по отдельности).

    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    
    len_dimensions = 8
    count_dimensions = 1
    
    # try:
    #     if len_dimensions*count_dimensions!=size:
    #         raise Exception
    # except Exception as e:
    #     print("Количество процессов должно быть равным произведению len_dimensions на count_dimensions")
    #     MPI.Finalize()
    ## HACKWIFI убери wifi ##

# dims -> размерность
# periods -> last ---> first
# reorder - rerank 012345
    comm_cart = comm.Create_cart(dims = (len_dimensions, count_dimensions), periods=(True, True), reorder = True) #Создаём оболочку топологии
    # dims (размер,длина) -> размер*длина == -n количество процессов (измерение и его длина должны соответствовать количеству процессов в нем)
    coords = comm_cart.Get_coords(rank=rank) # Берем координаты процесса в топологии

    #Для кольца
    if rank%2==0:
        sdata = rank
        # сдвигаем данные
        # Shift возвращает откуда, куда (ранги) вообще это право или лево, но мы считаем от 0 до n
        src, dest = comm_cart.Shift(direction=0,disp=2) #disp - величина сдвига(какому рангу процесса отправить curr+1), direction - номер измерения
        
        # print(f"rank - {rank}, coords - {coords}, src - {src}, dest - {dest}")
        # comm.Barrier() КАКОГО ТО ХРЕНА ЭТО ВЫЗЫВАЕТ ДЕДЛОК! ctrl + c в чат

        srdata = comm_cart.sendrecv(sendobj = sdata, dest = src, source = dest) # можно передавать только вещи с шифта, or будет дедлок)
        # у нас получается что. 2-4-6 2->6 а не 4->2 ==> scr-rank-dest. Вывод - не используем её. лучше простыми сенд рекв (Либо шизофрения, как у меня))))
        print(f"RING_rank - {rank}, data - {srdata}")
        comm.Barrier()

    #для звездочки (мастер - работяги) #bcast
    # корректнее по заданию наверное будет использовать sendrecv, но так проще, да и соответствует заданию.
    # http://www.hpcc.unn.ru/mskurs/RUS/DOC/ppr04.pdf 30 стр. требуется это синхронное с кольцом, но 2 топологии - не соответствие заданию.
    elif rank%2==1:
        if rank==1:
            sdata = rank
        else:
            sdata = rank
        
        sdata = comm.bcast(obj=sdata,root=1)
        
        print(f"Star_rank - {rank}, data - {sdata}")
        comm.Barrier() # делим сословия

    comm_cart.Free() # работяг нужно отпустить домой

# comm.Split()
# gsize= 
# grank= может быть так делить на comm.Group? но тогда нельзя использовать sendrecv, только по отдельности.
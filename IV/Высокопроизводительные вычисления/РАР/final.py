import multiprocessing as mp

def worker(start_city, end_city, city_all, city_not, q):
    n = len(city_all)
    temp = [[0] * n for _ in range(n)]
    
    # заполняем массив исключая ограничения
    for i in city_all:
        for j in city_all:
            if i != j and (i, j) not in city_not and (j, i) not in city_not:
                temp[i-1][j-1] = 1
    
    # https://www.geeksforgeeks.org/level-order-tree-traversal/ 
    # Алгоритм самой задачи
    def dfs(current, end, visited):
        if current == end:
            return True
        visited[current - 1] = True
        for neighbor in range(1, n + 1):
            if temp[current - 1][neighbor - 1] == 1 and not visited[neighbor - 1]:
                if dfs(neighbor, end, visited):
                    return True
        return False

    visited = [False] * n
    path_exists = dfs(start_city, end_city, visited)
    q.put(path_exists)

if __name__ == "__main__": #for Windows compatibility #https://calcul.math.cnrs.fr/attachments/spip/Documents/Ecoles/2013/python/Multiprocessing.pdf
    start_city = 1
    end_city = 8 #Молочный улун
    city_all = set(range(1, end_city + 1)) # Все сити
    city_not=[(1,2),(3,4),(5,6)] # Все сити, где я в бане
    
    q = mp.Queue() #Pipe повредит рез
    p = mp.Process(target=worker, args=(start_city, end_city, city_all, city_not, q))
    p.start()
    res = q.get()
    p.join()

    print(f"Path exists: {res}")
    
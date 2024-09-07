#include <iostream>
#include <omp.h>

using namespace std;

int main(){

    #pragma omp parallel num_threads(2)
    {
        #pragma omp signle
        {
            #pragma omp critical
            for (int i = 0; i<10;++i){
                cout << "B n_iteration: "<< i <<" //B num_thread: " << omp_get_thread_num() << endl;
            } 
        }
        cout << endl << "___________________\n" << endl;
        #pragma omp for nowait
        for (int i = 0; i<10;++i)
        {
            #pragma omp critical // nowait распределяет, critical - блокирует(для вывода, а по работе программы - все делает nowait(обе функции))
            cout << "A n_iteration: "<< i << " //A num_thread: " << omp_get_thread_num() << endl;
        }
    }

    return 0;
}
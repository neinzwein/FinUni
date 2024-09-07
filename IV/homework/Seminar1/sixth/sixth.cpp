#include <iostream>
#include <omp.h>

using namespace std;

int main(void)
{    
    #pragma omp parallel for
    for (int i = 0; i < 5; i++){
        for (int j = 0; j < 5; j++){
            printf("Thread number is %d\ni is %d\nj is %d\n", omp_get_thread_num(),i,j);
        }
    }
    cout << "_________\n"<<endl;
    #pragma omp parallel for collapse(2) // Количество размерностей цикла
    for (int i = 0; i < 5; i++){
        for (int j = 0; j < 5; j++){
            printf("Thread number is %d\ni is %d\nj is %d\n", omp_get_thread_num(),i,j);
        }
    }

    return 0;
}  
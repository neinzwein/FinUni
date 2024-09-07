#include <iostream>
#include <omp.h>

int main(){

    #pragma omp parallel num_threads(4)
    {
        #pragma omp sections
        {
            #pragma omp section
            {
            printf("First section :%d\n",omp_get_num_threads());
            }
            #pragma omp section
            {
                #pragma omp parallel
                {
                    printf("Second section :%d\n",omp_get_num_threads());
                    printf("Third section :%d\n",omp_get_num_threads());
                }
            }
            #pragma omp section
            {
                printf("Fourth section :%d\n",omp_get_num_threads());
            }
        }
    }

    return 0;
}
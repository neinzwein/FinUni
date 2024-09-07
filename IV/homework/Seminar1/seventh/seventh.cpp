#include <iostream>
#include <stdio.h>
#include <omp.h>

using namespace std;

int main(){

    int sum=0;
    #pragma omp parallel for num_threads(4)
    for (int i=1;i<=10;++i){
        sum+=i;
        printf("Anum_thread is %d\nSUM is %d\ni is %d\n",omp_get_thread_num(),i);
    }
    cout<<"_____\n"<<endl;
    sum=0;
    #pragma omp parallel for reduction(+ : sum)
    for (int i=1;i<=10;++i){
        sum+=i;
        printf("Bnum_thread is %d\nSUM is %d\ni is %d\n",omp_get_thread_num(),i);
    }

    return 0;
}
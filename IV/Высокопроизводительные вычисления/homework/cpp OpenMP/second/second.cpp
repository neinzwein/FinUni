#include <iostream>
#include <ctime>
#include <locale>
#include <vector>
#include <omp.h>

using namespace std;

int main(){

setlocale(LC_ALL, "ru");
    
    size_t vector_size = 500000001;

    vector <double> a(vector_size);
    vector <double> b(vector_size);
    vector <double> c(vector_size);

    clock_t start_t, end_t, total_t;

    start_t = clock();
    printf("Начало цикла инициализации векторов , start_t = %ld\n", start_t);

    for (auto &value : a){
        value = (double)rand() / RAND_MAX;
    }
    for (auto &value : b){
        value = (double)rand() / RAND_MAX;
    }

    end_t = clock();
    printf("Конец цикла инициализации векторов , end_t = %ld\n", end_t);
 
    total_t = end_t - start_t;
    cout << "Общее время работы процессора по инициализации векторов " << total_t / (CLOCKS_PER_SEC) << " seconds" << endl;
 
    start_t = clock();
    printf("Начало цикла сложения векторов , start_t = %ld\n", start_t);

    // Сложение векторов.
    #pragma omp parallel for shared(a,b,c)
    for (size_t i = 0; i<a.size();++i){
        c[i] = a[i] + b[i];
    }

    end_t = clock();
    printf("Конец цикла сложения векторов , end_t = %ld\n", end_t);
 
    total_t = end_t - start_t;
    cout << "Общее время работы процессора по сложению векторов " << total_t / (CLOCKS_PER_SEC) << " seconds" << endl;

    cout << c.size() << endl << c[100] << endl;

    return 0;
}
// быстрее. Не понимаю почему это же просто приватность.
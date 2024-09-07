#include <iostream>
#include <vector>
#include <ctime>
#include <omp.h>

#include <io.h>
#include <fcntl.h>

using namespace std;

int main() {

    _setmode(_fileno(stdout), _O_U16TEXT);
    
    size_t vector_size = 500000001;

    vector <double> a(vector_size);
    vector <double> b(vector_size);
    vector <double> c(vector_size);

    clock_t start_t, end_t, total_t;

/* Это объединение векторов. Я не понимаю, что нужно.
    a.insert(
        a.end(),
        make_move_iterator(b.begin()),
        make_move_iterator(b.end())
        );
    cout << a.size() << endl;
*/

    start_t = clock();
    wcout<<L"Начало цикла инициализации векторов , start_t = "<< start_t<<"\n"<<endl;

    for (auto &value : a){
        value = (double)rand() / RAND_MAX;
    }
    for (auto &value : b){
        value = (double)rand() / RAND_MAX;
    }

    end_t = clock();
    wcout<<L"Конец цикла инициализации векторов , end_t = "<< end_t<<"\n"<<endl;
 
    total_t = end_t - start_t;
    wcout <<L"Общее время работы процессора по инициализации векторов " << total_t / (CLOCKS_PER_SEC) << " seconds" << endl;
 
    start_t = clock();
    wcout<<L"Начало цикла сложения векторов , start_t = "<< start_t<<"\n"<<endl;

    // Сложение векторов.
    #pragma omp parallel for
    for (size_t i = 0; i<a.size();++i){
        c[i] = a[i] + b[i];
    }

    end_t = clock();
    wcout<<L"Конец цикла сложения векторов , end_t = "<<end_t<<"\n"<<endl;
 
    total_t = end_t - start_t;
    wcout << L"Общее время работы процессора по сложению векторов " << total_t / (CLOCKS_PER_SEC) << " seconds" << endl;

    wcout << c.size() << endl << c[100] << endl;

    return 0;
}

#include <iostream>
#include <omp.h>
#include <ctime>
#include <io.h>
#include <fcntl.h>

using namespace std;

int main(){

    _setmode(_fileno(stdout), _O_U16TEXT);

    time_t begin, end, result;
    
    begin = clock();
    wcout << L"Begin time" << endl;
    omp_set_nested(1);
    wcout << L"Разрешенные параллельные области "  << endl;
    #pragma omp parallel num_threads(2) //2 нити
    { //Секции, не понимаю как они работают по синтаксису.
        #pragma omp critical
        wcout << L"lvl1: " << omp_get_thread_num() << endl;

        #pragma omp parallel num_threads(2) //4 нити
        {
            #pragma omp critical
            wcout << L"lvl2: " << omp_get_thread_num() << endl;

            #pragma omp parallel num_threads(2) // 8 нитей
            {
                #pragma omp critical
                wcout << L"lvl3: " << omp_get_thread_num() << endl;

            }
        }
    }

    end = clock();
    result = end - begin;
    wcout << L"Total time: "<< result << endl;

    begin = clock();
    wcout << L"Begin time" << endl;
    wcout << L"Запрещенные параллельные области "  << endl;
    omp_set_nested(0);

    #pragma omp parallel num_threads(2)
    {
        #pragma omp critical
        wcout << L"lvl1: " << omp_get_thread_num() << endl;

        #pragma omp parallel num_threads(2)
        {
            #pragma omp critical
            wcout << L"lvl2: " << omp_get_thread_num() << endl;

            #pragma omp parallel num_threads(2)
            {
                #pragma omp critical
                wcout << L"lvl3: " << omp_get_thread_num() << endl;

            }
        }
    }

    end = clock();
    result = end - begin;
    wcout << L"Total time: "<< result << endl;

    return 0;

}
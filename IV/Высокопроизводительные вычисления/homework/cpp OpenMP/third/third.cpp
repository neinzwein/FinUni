#include <iostream>
#include <omp.h>

using namespace std;

int main(){
    int res = omp_get_max_threads();
    cout << "All threads: " << res << endl;

    # pragma omp parallel
    {
        #pragma omp for
        for (int n=0;n<10;++n){
            cout << omp_get_thread_num() << endl;
        }
    }
    return 0;
}
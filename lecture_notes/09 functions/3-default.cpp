
#include <iostream>
using namespace std;
// int main(int arvc, const char * argv[]){

// int max_(int a = 0, int b = 0) { return a > b ? a : b; };

// int main() {
//     cout << max_(10,20)<<'\n'<<max_(10)<<'\n'<<max_( - 20);
// }
// cin.get();
// return 0;
// }
int max_(int a = 0, int b = 0) { return a > b ? a : b; }

int main() {

    cout << "[" << max_(10,20)<<", "<<max_(10)<<", "<<max_( - 20)<< "]"<< endl;

    return 0;
}
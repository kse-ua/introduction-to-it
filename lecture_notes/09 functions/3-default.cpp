#include <iostream>
using namespace std;

int max(int a = 0, int b = 0){
    return a > b ? a : b;
}

int main() {
    cout << max(10, 30) << ' ';
    cout << max(10) << ' ';
    cout << max(-20) << endl;
}


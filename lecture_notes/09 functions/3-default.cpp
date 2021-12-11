#include <iostream>
using namespace std;

int max_value(int a = 0, int b = 0) {

    if (a > b) {
        return a;
    } else {
        return b;
    }
}

int main() {

    cout << max_value(10, 20) << ' ';
    cout << max_value(10) << ' ';
    cout << max_value(-20) << endl;

    return 0;  
}

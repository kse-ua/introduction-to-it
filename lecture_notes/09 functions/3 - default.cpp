using namespace std;
#include <iostream>https://github.com/DenisMilkevich/introduction-to-it/tree/Labb_9

int max(int a = 0, int b = 0) {
    return a > b ? a : b;
}

int main() {
    cout << max(10, 20) << endl;
    cout << max(10) << endl;
    cout << max(-20) << endl;
}

#include <iostream>
using namespace std;

auto maximum = [](int a = 0, int b = 0) -> int { return a > b ? a : b; };

int main() {
    cout << maximum(10, 20) << endl;
    cout << maximum(10) << endl;
    cout << maximum(-20) << endl;
}

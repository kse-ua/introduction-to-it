#include <iostream>

using namespace std;

int main() {
    auto max = [](int a = 0, int b = 0) {
        return a > b ? a : b;
    };

    cout << max(10, 20) << " " << max(10) << " " << max(-10) << endl;

    return 0;
}

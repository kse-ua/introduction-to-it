#include <iostream>
#include <map>
using namespace std;

int addFunction(int a, int b) {
    int res = a + b;
    return res;
}

int addProcedure(int a, int b) {

    map < string, int > cache;
    std::string keyValue = std::to_string(a) + "," + std::to_string(b);

    cache[keyValue] = 0;
    int res = cache[keyValue];
    if (res != 0) {
        return res;
    }
    res = a + b;
    cache[keyValue] = res;
    return res;
}

int main() {
    cout << "addProcedure: " << addProcedure(10, 20) << endl;
    cout << "addFunction: " << addFunction(10, 20) << endl;
    cout << "addProcedure: " << addProcedure(100, 20) << endl;
    cout << "addFunction: " << addFunction(100, 20) << endl;
    return 0;
}

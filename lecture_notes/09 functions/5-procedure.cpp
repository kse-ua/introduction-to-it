// Online C++ compiler to run C++ program online
#include <iostream>
#include <vector>
#include <map>
using namespace std;

int addFunction(int x, int y) {
    int result = x + y;
    return result;
}

map <string, int> cache = {};

int addProcedure(int x, int y) {
    string key = to_string(x) + ',' + to_string(y);
    if (cache.count(key) == 1) {
        cout << "It works!" << " ";
        return cache[key];
    }
    else{
    int result = x + y;
    cache[key] = result;
    return result;
    }
}

int main() {
    cout << addFunction(10, 20) << " ";
    cout << addFunction(100, 200) << " ";
    cout << addFunction(1, 2) << " ";
    cout << addFunction(10, 20) << " ";
    cout << addProcedure(10, 20) << " ";
    cout << addProcedure(100, 200) << " ";
    cout << addProcedure(1, 2) << " ";
    cout << addProcedure(10, 20) << " ";
}

using namespace std;
#include <iostream>
#include <map>


int addFunction(int a, int b) {
    auto result = a + b;
    return result;
}

map <string, int> cache;

int addProcedure(int a, int b) {
    string key = to_string(a) + ',' + to_string(b);
    if (cache.count(key) == 1) {
        return cache[key];
    }
    int result = a + b;
    cache[key] = result;
    return result;
}

int main() {
    cout << addFunction(10, 20) << " " << addFunction(1,2) << " ";
    cout << addFunction(100, 20) << " " << addFunction(100, 200) << endl;
    cout << addProcedure(10, 20) << " " << addProcedure(1,2) << " ";
    cout << addProcedure(100, 20) << " " << addProcedure(100, 200) << endl;
}

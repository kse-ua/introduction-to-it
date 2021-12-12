using namespace std;
#include <iostream>
#include <map>

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

int subProcedure(int a, int b) {
    string key = to_string(a) + ',' + to_string(b);
    if (cache.count(key) == 1) {
        return cache[key];
    }
    int result = a - b;
    cache[key] = result;
    return result;
}


int main() {
    cout << "sub:" << subProcedure(5, 2) << endl;
    cout << "add:" << addProcedure(5, 2) << endl;
}

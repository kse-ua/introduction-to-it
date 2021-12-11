using namespace std;
#include <iostream>
#include <map>

int addProcedure(int a, int b);
int subProcedure(int a, int b);

map<string, int> cache;

int main() {
    cout << "sub: " << subProcedure(5, 2) << endl;
    cout << "add: " << addProcedure(5, 2) << endl;
}

int addProcedure(int a, int b) {
    string key = to_string(a) + ',' + to_string(b);
    if (cache.count(key) == 1) {
        return cache[key];
    }
    int res = a + b;
    cache[key] = res;
    return res;
}

int subProcedure(int a, int b) {
    string key = to_string(a) + ',' + to_string(b);
    if (cache.count(key) == 1) {
        return cache[key];
    }
    int res = a - b;
    cache[key] = res;
    return res;
}




#include <iostream>
#include <map>
#include <sstream>
using namespace std;

map<string, int> cache;

int addFunction(int a, int b) {
    return a + b;
}

int addProcedure(int a, int b) {
    ostringstream tempKey;
    tempKey << a << "," << b;
    string key = tempKey.str();
    if (cache.count(key) == 1) {
        return cache[key];
    }
    int res = a + b;
    cache[key] = res;
    return res;
}

int subProcedure(int a, int b) {
    ostringstream tempKey;
    tempKey << a << "," << b;
    string key = tempKey.str();
    if (cache.count(key) == 1) {
        return cache[key];
    }
    int res = a - b;
    cache[key] = res;
    return res;
}

int main() {
    printf("sub: %d\n", subProcedure(5, 2));
    printf("add: %d", addProcedure(5, 2));
    return 0;
}

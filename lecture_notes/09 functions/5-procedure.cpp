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

int main() {
    printf("%d, ", addFunction(10, 20));
    printf("%d, ", addFunction(1, 2));
    printf("%d, ", addFunction(100, 20));
    printf("%d\n", addFunction(100, 200));
    printf("%d, ", addProcedure(10, 20));
    printf("%d, ", addProcedure(1, 2));
    printf("%d, ", addProcedure(100, 20));
    printf("%d ", addProcedure(100, 200));
    return 0;
}

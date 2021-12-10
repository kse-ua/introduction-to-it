#include <iostream>  
#include <string>  
#include <map>
using namespace std;  

map <string, int> cache;

int addProcedure(int a, int b) {
    string key = to_string(a) + ", " +to_string(b);
    if (cache.count(key) == 1) {
        return cache[key];
    }
    int res = a + b;
    cache[key] = res;
    return res;
}

int subProcedure(int a, int b) {
    string key = to_string(a) + ", " +to_string(b);
    if (cache.count(key) == 1) {
        return cache[key];
    }
    int res = a - b;
    cache[key] = res;
    return res;
}

int main() {
    printf("sub: %d\n", subProcedure(5, 2));
    printf("add: %d\n", addProcedure(5, 2));  
}

// the code is actually not working properly
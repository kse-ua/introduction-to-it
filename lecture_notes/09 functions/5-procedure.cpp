#include <iostream>  
#include <string>  
#include <map>
using namespace std;  

int addFunction(int a, int b) {
    return a + b;   
}

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

int main () {
    printf("%d\n", addFunction(10, 20));
    printf("%d\n", addFunction(1, 2));
    printf("%d\n", addFunction(100, 20));
    printf("%d\n", addFunction(100, 200));
    printf("%d\n", addProcedure(10, 20));
    printf("%d\n", addProcedure(1, 2));
    printf("%d\n", addProcedure(100, 20));
    printf("%d\n", addProcedure(100, 200));
    // somehow print cache
}

// the code is actually not working properly
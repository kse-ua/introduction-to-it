#include <iostream>
#include <stdio.h>
#include <string>
#include <map>

int addFunction(int a, int b) {
    int res = a + b;
    return res;
};

// Created map
// (key, value) like object in js
std::map<std::string, int> cache;

int addProcedure (int a, int b) {
    std::string key = a + "," + b;

    if (cache.contains(key)){
        return cache[key];
    }

    int res = a + b;
    cache[key] = res;
    return res;
};

int main(){

    printf("%d\n", addFunction(10, 20));
    printf("%d\n", addFunction(1, 2));
    printf("%d\n", addFunction(100, 20));
    printf("%d\n", addFunction(100, 200));

    printf("%d\n", addProcedure(10, 20));
    printf("%d\n", addProcedure(1, 2));
    printf("%d\n", addProcedure(100, 20));
    printf("%d\n", addProcedure(100, 200));
    return 0;
}

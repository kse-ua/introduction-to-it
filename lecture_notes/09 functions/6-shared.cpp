#include <iostream>
#include <stdio.h>
#include <string>
#include <map>

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


int subProcedure (int a, int b) {
    std::string key = a + "," + b;

    if (cache.contains(key)){
        return cache[key];
    }

    int res = a - b;
    cache[key] = res;
    return res;

};


int main(){
    printf("sub: %d\n", subProcedure(5, 2));
    printf("add: %d\n", addProcedure(5, 2));
    return 0;
}

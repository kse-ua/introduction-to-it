#include <iostream>
#include <map>
#include <string>

using namespace std;

int cached_add(int a, int b, map<string, int>& cache) {
    string key = to_string(a) + "+" + to_string(b);
    auto cached_result = cache.find(key);

    int result;
    if (cached_result == cache.end()) {
        result = a + b;
        cache[key] = result;
    } else {
        result = cached_result->second;
    }

    return result;
}

int cached_sub(int a, int b, map<string, int>& cache) {
    string key = to_string(a) + "-" + to_string(b);
    auto cached_result = cache.find(key);

    int result;

    if (cached_result == cache.end()) {
        result = a - b;
        cache[key] = result;
    } else {
        result = cached_result->second;
    }

    return result;
}


int main() {
    map<string, int> cache;

    cout << "sub: " << cached_sub(5, 2, cache) << endl;
    cout << "add: " << cached_add(5, 2, cache) << endl;
    return 0;
}
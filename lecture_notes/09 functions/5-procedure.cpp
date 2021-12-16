#include <iostream>
#include <map>
#include <string>

using namespace std;

int add(int a, int b) {
    return a + b;
}

int cached_add(int a, int b, map<string, int>& cache) {
    string key = to_string(a) + "," + to_string(b);
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


int main() {
    map<string, int> cache;

    cout << add(10, 20) << ", "
         << add(1, 2) << ", "
         << add(100, 20) << ", "
         << add(100, 200) << endl;

    cout << cached_add(10, 20, cache) << ", "
         << cached_add(1, 2, cache) << ", "
         << cached_add(100, 20, cache) << ", "
         << cached_add(100, 200, cache) << endl;

    return 0;
}


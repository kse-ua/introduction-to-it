#include <iostream>
#include <map>
using namespace std;

// Similar to (include vector), but can store 2 values
map <string, int> cache;

int add_procedure(int a, int b) {

    string first = to_string(a);
    string second = to_string(b);
    string key = first + ',' + second;

    if (cache.count(key) == 1) {
        return cache[key];
    }

    int res = a + b;
    cache[key] = res;

    return res;
}

int sub_procedure(int a, int b) {

    string first = to_string(a);
    string second = to_string(b);
    string key = first + ',' + second;

    if (cache.count(key) == 1) {
        return cache[key];
    }

    int res = a - b;
    cache[key] = res;
    
    return res;
}

int main() {

    cout << "sub: " << sub_procedure(5, 1) << endl;
    cout << "add: " << add_procedure(5, 3) << endl;

    return 0;
}

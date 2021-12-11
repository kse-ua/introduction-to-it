#include <iostream>
#include <map>
using namespace std;

// Similar to (#include <vector>), but can store 2 values
map <string, int> cache;

int add_function(int a, int b) {

    int res = a + b;
    return res;
}

int add_procedure(int a, int b) {

    string first = to_string(a);
    string second = to_string(b);
    string key = first + ',' + second;

    // Returns number of occurrences of an element
    if (cache.count(key) == 1) {
        return cache[key];
    }

    int res = a + b;
    cache[key] = res;
    return res;
}

int main() {

    // add_function console output
    cout << "[ ";
    cout << add_function(10, 20) << " ";
    cout << add_function(1,2) << " ";
    cout << add_function(100, 20) << " ";
    cout << add_function(100, 200);
    cout << " ]" << endl;

    // add_procedure console output
    cout << "[ ";
    cout << add_procedure(10, 20) << " ";
    cout << add_procedure(1,2) << " ";
    cout << add_procedure(100, 20) << " ";
    cout << add_procedure(100, 200);
    cout << " ]" << endl;

    return 0;
}

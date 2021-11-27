#include <iostream>
#include <set>

using namespace std;

void print_set(const set<int>& s) {
    cout << "set(" << s.size() << ") { ";
    for (auto item : s) {
        cout << item << " ";
    }
    cout << "}" << endl;
}

int main() {
    set<int> ages {10, 12, 15, 15, 17, 18, 18, 19, 20};
    print_set(ages);

    ages.insert(16);
    ages.erase(20);

    int values[]  = {10, 16, 19, 20};
    int values_length = sizeof(values) / sizeof(int);
    bool has_element;

    cout << boolalpha;
    for (size_t i = 0; i < values_length; i++) {
        int value = values[i];
        bool has_element = ages.find(value) != ages.end();
        cout << values[i] << ": " << has_element << endl;
    }

    ages.clear();
    print_set(ages);

    return 0;
}

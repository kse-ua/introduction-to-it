#include <algorithm>
#include <functional>
#include <iostream>
#include <vector>

using namespace std;

void f1();

template<class T>
void print_vector(const vector<T>& v, const string& comment) {
    cout << comment << " [ ";
    for (const auto& e : v) {
        cout << e << " ";
    }
    cout << "]" << endl;
}

int main() {
    vector<string> cities {"Athens", "Roma", "London", "Beijing", "Kiev", "Riga"};
    auto f = [](const string& s) {
        return s.length();
    };

    f1();

    print_vector(cities, "cities:");
    vector<size_t> modified_cities(cities.size());
    transform(cities.begin(), cities.end(), modified_cities.begin(), f);
    print_vector(modified_cities, "modified cities:");

    return 0;
}

void f1() {
    vector<string> cities {"Athens", "Roma"};
    auto f = [](string s) {
        transform(s.begin(), s.end(), s.begin(), ::toupper);
        return s;
    };

    print_vector(cities, "cities:");

    vector<string> modified_cities(cities.size());
    transform(cities.begin(), cities.end(), modified_cities.begin(), f);
    print_vector(modified_cities, "upper cities:");

    {
        auto f = [](string s) {
            transform(s.begin(), s.end(), s.begin(), ::tolower);
            return s;
        };
        vector<string> modified_cities(cities.size());
        transform(cities.begin(), cities.end(), modified_cities.begin(), f);
        print_vector(cities, "cities:");
        print_vector(modified_cities, "lower cities:");

    }
    {
        vector<string> cities {"London", "Beijing", "Kiev"};
        print_vector(cities, "cities:");
        vector<string> modified_cities(cities.size());
        transform(cities.begin(), cities.end(), modified_cities.begin(), f);
        print_vector(modified_cities, "upper cities:");
    }
}

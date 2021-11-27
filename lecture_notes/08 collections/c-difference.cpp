#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

void print_vector(const vector<string>& v, const string& comment) {
    cout << comment << " [ ";
    for (const auto& e : v) {
        cout << e << " ";
    }

    cout << "]" << endl;
}

vector<string> difference(const vector<string>& v1, const vector<string> v2) {
    vector<string> v;
    size_t max_size = v2.size();
    v.reserve(max_size);
    size_t actual_size = 0;
    for (const auto& s: v1) {
         if (find(v2.begin(), v2.end(), s) == v2.end()) {
            v.push_back(s);
            actual_size++;
        }
    }

    v.resize(actual_size);

    return v;
}

vector<string> fast_difference(vector<string> v1, vector<string> v2) {
    vector<string> v(v2.size());
    sort(v1.begin(), v1.end());
    sort(v2.begin(), v2.end());
    auto end_it = set_difference(v1.begin(), v1.end(), v2.begin(), v2.end(), v.begin());
    v.resize(end_it - v.begin());

    return v;
}

int main() {
    vector<string> cities1 {"Beijing", "Kiev"};
    vector<string> cities2 {"Kiev", "London", "Baghdad"};
    print_vector(cities1, "cities1:");
    print_vector(cities2, "cities2:");

    auto difference_result = difference(cities1, cities2);
    auto fast_difference_result = fast_difference(cities1, cities2);
    print_vector(difference_result, "difference:");
    print_vector(fast_difference_result, "fast difference:");

    return 0;
}

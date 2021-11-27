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

vector<string> vector_union(const vector<string>& v1, const vector<string> v2) {
    vector<string> v = v1;
    size_t initial_size = v1.size();
    size_t max_size = initial_size + v2.size();
    v.reserve(max_size);

    size_t actual_size = initial_size;
    for (const auto& s: v2) {
         if (find(v.begin(), v.end(), s) == v.end()) {
            v.push_back(s);
            actual_size++;
        }
    }

    v.resize(actual_size);

    return v;
}

vector<string> fast_union(vector<string> v1, vector<string> v2) {
    vector<string> v(v1.size() + v2.size());
    sort(v1.begin(), v1.end());
    sort(v2.begin(), v2.end());
    auto end_it = set_union(v1.begin(), v1.end(), v2.begin(), v2.end(), v.begin());
    v.resize(end_it - v.begin());

    return v;
}

int main() {
    vector<string> cities1 {"Beijing", "Kiev"};
    vector<string> cities2 {"Kiev", "London", "Baghdad"};
    print_vector(cities1, "cities1:");
    print_vector(cities2, "cities2:");

    auto union_result = vector_union(cities1, cities2);
    auto fast_union_result = fast_union(cities1, cities2);
    print_vector(union_result, "union:");
    print_vector(fast_union_result, "fast union:");

    return 0;
}

#include <iostream>
#include <vector>
#include <utility>

using namespace std;

pair<int, int> get_first_and_last(const vector<int>& array) {
    int first = array[0];
    int last = array[array.size() - 1];
    return { first, last };
}


int main() {
    vector<int> ages{ 10, 12, 15, 15, 17, 18, 18, 19, 20 };

    auto first_and_last = get_first_and_last(ages);

    cout << "first: " << first_and_last.first << endl;
    cout << "last: " << first_and_last.second << endl;

    return 0;
}
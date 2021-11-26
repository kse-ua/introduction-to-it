#include <vector>
#include <iostream>

using namespace std;

int main() {
    vector<int> ages{ 10, 12, 15, 15, 17, 18, 18, 19, 20 };

    ages.erase(ages.begin());
    ages.insert(ages.begin(), 5);

    ages.pop_back();
    ages.push_back(10);

    int length = ages.size();
    int first = ages[0];
    int last = ages[length - 1];


    cout << "first: " << first << endl;
    cout << "last: " << last << endl;

    return 0;
}

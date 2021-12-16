#include <iostream>
using namespace std;

// Creating a nested array, where a number with index 0 - x, 1 - y
int polyline[4][2] ={{0, 0}, {10, 10}, {20, 20}, {30, 30}};

// Using a camelCase for function names
int initialPoint() {

    // Outputting values from polyline in an appropriate format
    for (auto & i : polyline) {
        for (int j = 0; j < 2; ++j) {
            if (j == 0) {
                cout << "x, y = " << i[j];
            } else {
                cout << ", " << i[j] << "\n";
            }
        }
    }
    return 0;
}

int addingValues(const int arr[]) {
    cout << "\n" << "Adding new values ..." << endl << "\n";

    for (auto & i : polyline) {
        for (int j = 0; j < 2; ++j) {
            if (j == 0) {
                cout << "x, y = " << i[j];
            } else {
                i[j] += arr[j];
                cout << ", " << i[j] << "\n";
            }
        }
    }
    return 0;
}

int main() {
    int arr[] = {10, -5};
    initialPoint();
    addingValues(arr);
    return 0;
}
